#!/usr/bin/env python

import json
from html import escape
from urllib.parse import parse_qs, urlencode
from wsgiref.simple_server import make_server
import pandas as pd
from helper import get_database_session, init_mysql_engine, compute_best_lineup
from models import Player

MYSQL_USER = 'root'
MYSQL_PWD = ''
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DB = 'fifa'

# from pprint import pprint

# METHODS
# CONTENT TYPES
# STATUS
# GENERIC MESSAGES
# PATHS

## DONE: normalize column names
## DONE: sqlalchemy ORM
## DONE: sqlalchemy session
## DONE: MySQL
## DONE: sqlalchemy querying: name, club & nationality
## DONE: sqlalchemy in wsgi
## DONE: prep response:  Name, Age, Nationality, Club, Photo (should display it), Overall (score), Value
## DONE: fix photo links


engine = init_mysql_engine(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

def decode_byte_dict(payload):
  result = {}

  for key, value in payload.items():
    key_decoded = key.decode('UTF-8')
    value_decoded = value[0].decode('UTF-8') if len(value) < 2 else [v.decode('UTF-8') for v in value]
    result[key_decoded] = value_decoded

  return result

def application (environ, start_response):

    session = get_database_session(engine)

    json_c_type = "application/json"

    paths = [p for p in environ['PATH_INFO'].split('/') if p != '']

    headers = []
    origin = environ.get("HTTP_ORIGIN")
    method = environ['REQUEST_METHOD']

    cors = origin
    preflight = cors and method == "OPTIONS"
    if cors:
      headers.append(("Access-Control-Allow-Origin", origin))
      if preflight:
        headers.extend([
            ("Access-Control-Allow-Methods", "POST"),
            ("Access-Control-Allow-Headers", "Content-Type")
        ])

    # /
    if len(paths) == 0:

      status = '200 OK'
      headers.append(('Content-Type', json_c_type))
      payload = {f'message': f"Server works!"}
      response = json.dumps(payload, indent=4)

      start_response(status, headers)

      return [response.encode()]

    else:
      # /players/
      if paths[0] == 'players':

        # GET: /players/
        if method == 'GET':

          # GET: /players/
          if len(paths) == 1:
            try:
              # query extract
              query = parse_qs(environ['QUERY_STRING'])
              name = query.get('name', [''])[0]
              club = query.get('club', [''])[0]
              nationality = query.get('nationality', [''])[0]
              limit = int(query.get('limit', [10])[0])
              skip = int(query.get('skip', [0])[0])

              rows_all = session.query(Player)

              if name != '':
                rows_all = rows_all.filter(Player.name.ilike(f'%{name}%'))
              if club != '':
                rows_all = rows_all.filter(Player.club.ilike(f'%{club}%'))
              if nationality != '':
                rows_all = rows_all.filter(Player.nationality.ilike(f'%{nationality}%'))

              rows_all = rows_all.order_by(Player.overall.desc(), Player.value.desc())

              rows =  rows_all \
                        .offset(skip) \
                        .limit(limit)

              # result set
              records = [dict(id=r.id, name=r.name, position=r.position, nationality=r.nationality,
                              flag=r.flag, club=r.club, age=r.age, photo=r.photo,
                              value=r.value, overall=r.overall )
                        for r in rows]

              # 'next': urlencode # f"{environ['SERVER_NAME']}:{environ['SERVER_PORT']}/{module}/? ",
              status = '200 OK'
              headers.append(('Content-Type', json_c_type))
              payload = {
                'count': rows_all.count(),
                'results': records
              }
              response = json.dumps(payload, indent=4)

              start_response(status, headers)

              return [response.encode()]

            except Exception:
              status = '500 Internal Server Error'
              headers.append(('Content-Type', json_c_type))
              payload = {f'message': f"Oops! Something went wrong!"}

              response = json.dumps(payload, indent=4)

              start_response(status, headers)

              return [response.encode()]


          # GET: /players/...
          else:
            status = '403 Forbidden'
            headers.append(('Content-Type', json_c_type))
            payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

            response = json.dumps(payload, indent=4)

            start_response(status, headers)

            return [response.encode()]

        # POST: /players/
        elif method == 'POST':

          # POST: /players/team/
          if len(paths) == 2 and paths[1] == 'team':

            length = int(environ.get('CONTENT_LENGTH', '0'))
            request_body = environ['wsgi.input'].read(length)
            body = json.loads(request_body)
            # verify
            formation = body.get('formation', None)
            budget = int(body.get('budget', 0))

            if formation is not None and budget >= 1 * 10**6:

              try:

                formation = [ f.lower() for f in formation]

                temp = pd.read_sql_table('players', con=engine)[['id', 'position', 'value', 'overall']] \
                        .dropna(subset=['position']) \
                        .query(f'position in {formation} and value > 0')

                prob, ids = compute_best_lineup(temp, formation, budget)

                rows = session.query(Player).filter(Player.id.in_(ids))

                records = { r.position: dict(id=r.id, name=r.name, position=r.position, nationality=r.nationality,
                                             flag=r.flag, club=r.club, age=r.age, photo=r.photo,
                                              value=r.value, overall=r.overall )
                            for r in rows}
                status = '200 OK'
                headers.append(('Content-Type', json_c_type))
                payload = {
                  'total_overall': sum([r.overall for r in rows]),
                  'total_value': sum([r.value for r in rows]),
                  'formation': formation,
                  'results': records
                }

                response = json.dumps(payload, indent=4)

                start_response(status, headers)

                return [response.encode()]

              except Exception:

                status = '500 Internal Server Error'
                headers.append(('Content-Type', json_c_type))
                payload = {f'message': f"Oops! Something went wrong!"}

                response = json.dumps(payload, indent=4)

                start_response(status, headers)

                return [response.encode()]


            else:

              status = '400 Bad Request'
              headers.append(('Content-Type', json_c_type))
              payload = {
                'message': f"Please select 11 unique and valid positions and set budget greater than € 1,000,000!",
                'formation': formation,
                'budget': budget
              }

              response = json.dumps(payload, indent=4)

              start_response(status, headers)

              return [response.encode()]

          # POST: /players/...
          else:

            status = '403 Forbidden'
            headers.append(('Content-Type', json_c_type))
            payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

            response = json.dumps(payload, indent=4)

            start_response(status, headers)

            return [response.encode()]

        # HEAD: /players/
        elif method == 'HEAD':
          status = '200 OK'

          start_response(status, headers)

          return []

        # HEAD: /players/
        elif method == 'OPTIONS':
          status = '200 OK'

          start_response(status, headers)

          return []

        # PUT/DELETE/PATCH/OPTIONS: /players/
        else:
          status = '405 Method Not Allowed'
          headers.append(('Content-Type', json_c_type))
          payload = {f'message': f"You are not allowed to make request with {environ['REQUEST_METHOD']} to `{environ['PATH_INFO']}`!"}

          response = json.dumps(payload, indent=4)

          start_response(status, headers)

          return [response.encode()]


      # /assets/
      elif paths[0] == 'assets':

        # TODO: if get
        # TODO: if none found
        status = '200 OK'
        headers.append(('Content-Type', 'image/png'))

        start_response(status, headers)

        return [open(f"./{environ['PATH_INFO']}", "rb").read()]

      # /*
      else:
        status = '403 Forbidden'
        headers.append(('Content-Type', json_c_type))
        payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

        response = json.dumps(payload, indent=4)

        start_response(status, headers)

        return [response.encode()]


if __name__ == "__main__":

  httpd = make_server('localhost', 8051, application)

  # Now it is serve_forever() in instead of handle_request()
  httpd.serve_forever()
