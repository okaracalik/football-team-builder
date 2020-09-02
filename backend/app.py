#!/usr/bin/env python

import json
from html import escape
from pprint import pprint
from urllib.parse import parse_qs, urlencode
from wsgiref.simple_server import make_server

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player

MYSQL_USER = 'root'
MYSQL_PWD = ''
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DB = 'fifa'

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


def init_mysql_engine(user, pwd, host, port, db):
  return create_engine(f'mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}')


def get_database_session(engine):
  Session = sessionmaker(bind=engine)
  return Session()

engine = init_mysql_engine(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

def application (environ, start_response):

    session = get_database_session(engine)

    json_c_type = "application/json"

    paths = [p for p in environ['PATH_INFO'].split('/') if p != '']

    headers = []
    origin = environ.get("HTTP_ORIGIN")

    cors = origin
    if cors:
      headers.append(("Access-Control-Allow-Origin", origin))

    if len(paths) == 0:
      status = '200 OK'
      headers.append(('Content-Type', json_c_type))
      payload = {f'message': f"Server works!"}
      response = json.dumps(payload, indent=4)

      start_response(status, headers)

      return [response.encode()]

    else:
      if paths[0] == 'players':

        method = environ['REQUEST_METHOD']

        if method == 'GET':

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
              records = [dict(id=r.id, name=r.name, nationality=r.nationality,
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

          elif len(paths) == 2:
            ## DONE: img
            ## TODO: get by id
            ## TODO: team builder
            status = '501 Not Implemented'
            headers.append(('Content-Type', json_c_type))
            payload = {'message': f"Method not implemented yet for `{environ['PATH_INFO']}`!", 'path': paths}

            response = json.dumps(payload, indent=4)

            start_response(status, headers)

            return [response.encode()]

          else:
            status = '403 Forbidden'
            headers.append(('Content-Type', json_c_type))
            payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

            response = json.dumps(payload, indent=4)

            start_response(status, headers)

            return [response.encode()]

        elif method == 'HEAD':
          status = '200 OK'

          start_response(status, headers)

          return []

        else:
          status = '405 Method Not Allowed'
          headers.append(('Content-Type', json_c_type))
          payload = {f'message': f"You are not allowed to make request with {environ['REQUEST_METHOD']} to `{environ['PATH_INFO']}`!"}

          response = json.dumps(payload, indent=4)

          start_response(status, headers)

          return [response.encode()]


      elif paths[0] == 'assets':

        status = '200 OK'
        headers.append(('Content-Type', 'image/png'))

        start_response(status, headers)

        return [open(f"./{environ['PATH_INFO']}", "rb").read()]

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
