#!/usr/bin/env python

import json
from html import escape
from urllib.parse import parse_qs, urlencode
from wsgiref.simple_server import make_server
from os import stat

import pandas as pd

from helper import compute_best_lineup, get_database_session, init_mysql_engine
from models import Player
from response import ResponseFactory

POSITIONS = [
  'ls', 'st', 'rs',
  'lw', 'lf', 'cf', 'rf', 'rw',
  'lam', 'cam', 'ram',
  'lm', 'lcm', 'cm', 'rcm', 'rm',
  'lwb', 'ldm', 'cdm', 'rdm', 'rwb',
  'lb', 'lcb', 'cb', 'rcb', 'rb',
  'gk'
]

try:
  with open('./config.json', 'r') as f:
    CONFIG = json.load(f)

  engine = init_mysql_engine(CONFIG['MYSQL_USER'],
                            CONFIG['MYSQL_PWD'],
                            CONFIG['MYSQL_HOST'],
                            CONFIG['MYSQL_PORT'],
                            CONFIG['MYSQL_DB'])
except Exception as e:
  print('Server Configuration Error: ', e)

def application (environ, start_response):

    session = get_database_session(engine)

    json_c_type = "application/json"

    paths = [p for p in environ['PATH_INFO'].split('/') if p != '']

    headers = []
    origin = environ.get("HTTP_ORIGIN")
    method = environ['REQUEST_METHOD']

    response_factory = ResponseFactory()

    # /
    if len(paths) == 0:

      payload = {f'message': f"Server works!"}

      return response_factory \
              .create(200) \
              .get_response(payload, start_response)

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

              payload = {
                'count': rows_all.count(),
                'results': records
              }

              return response_factory \
                      .create(200, origin, method) \
                      .get_response(payload, start_response)

            except Exception as e:

              payload = {f'message': f"Oops! Something went wrong! => {e}"}

              return response_factory \
                      .create(500) \
                      .get_response(payload, start_response)


          # GET: /players/...
          else:

            payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

            return response_factory \
                    .create(403) \
                    .get_response(payload, start_response)

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
            include_free_agents = body.get('include_free_agents', True)

            if formation and all([p in POSITIONS for p in formation]) and budget >= 1 * 10**6:

              try:

                formation = [ f.lower() for f in formation]

                temp = pd.read_sql_table('players', con=engine)[['id', 'position', 'value', 'overall']] \
                        .dropna(subset=['position']) \
                        .query(f'position in {formation}')

                temp = temp if include_free_agents else temp.query('value > 0')

                prob, ids = compute_best_lineup(temp, formation, budget)

                rows = session.query(Player).filter(Player.id.in_(ids))

                records = { r.position: dict(id=r.id, name=r.name, position=r.position, nationality=r.nationality,
                                             flag=r.flag, club=r.club, age=r.age, photo=r.photo,
                                              value=r.value, overall=r.overall )
                            for r in rows}

                payload = {
                  'total_overall': sum([r.overall for r in rows]),
                  'total_value': sum([r.value for r in rows]),
                  'formation': formation,
                  'results': records
                }

                return response_factory \
                        .create(200, origin, method) \
                        .get_response(payload, start_response)

              except Exception as e:

                payload = {f'message': f"Oops! Something went wrong! => {e}"}

                return response_factory \
                        .create(500) \
                        .get_response(payload, start_response)


            else:

              payload = {
                'message': f"Please select 11 unique and valid positions and set budget greater than € 1,000,000!",
                'formation': formation,
                'budget': budget
              }

              return response_factory \
                        .create(400) \
                        .get_response(payload, start_response)

          # POST: /players/...
          else:

            payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

            return response_factory \
                    .create(403) \
                    .get_response(payload, start_response)

        # HEAD/OPTIONS: /players/
        elif method == 'HEAD' or  method == 'OPTIONS':

          return response_factory \
                    .create(200, origin, method) \
                    .get_response(None, start_response)

        # PUT/DELETE/PATCH/OPTIONS: /players/
        else:

          payload = {f'message': f"You are not allowed to make request with {environ['REQUEST_METHOD']} to `{environ['PATH_INFO']}`!"}

          return response_factory \
                  .create(405) \
                  .get_response(payload, start_response)


      # /assets/
      elif paths[0] == 'assets':

        if method == 'GET':
          status = '200 OK'


          try:
            headers.append(('Content-Type', 'image/png'))

            start_response(status, headers)

            with open(f"./{environ['PATH_INFO']}", "rb") as f:
              img = f.read()
              size = stat(f"./{environ['PATH_INFO']}").st_size

            if size == 0:
              with open(f"./assets/players/000000.png", "rb") as f:
                img = f.read()

            return [img]

          except Exception as e:

            payload = {'message': f"Image is not available! => {e}"}

            return response_factory \
                    .create(404) \
                    .get_response(payload, start_response)

          else:

            payload = {f'message': f"You are not allowed to make request with {environ['REQUEST_METHOD']} to `{environ['PATH_INFO']}`!"}

            return response_factory \
                    .create(405) \
                    .get_response(payload, start_response)

      # /*
      else:

        payload = {'message': f"You are not allowed to make request to `{environ['PATH_INFO']}`!"}

        return response_factory \
                .create(403) \
                .get_response(payload, start_response)


if __name__ == "__main__":

  try:

    HOST = '0.0.0.0'
    PORT = 8051
    httpd = make_server(HOST, PORT, application)

    print('Server running!')
    print(f'http://localhost:{PORT}')

    httpd.serve_forever()

  except Exception as e:
    print('Server Error: ', e)
