import json

CONTENT_TYPE_JSON = "application/json"

class Response(object):
  status = ""
  headers = []
  payload = None
  callback = None

  def __init__(self, origin, method):
    cors = origin
    preflight = cors and method == "OPTIONS"

    if cors:
      self.headers = [("Access-Control-Allow-Origin", origin)]
      if preflight:
        self.headers.extend([
            ("Access-Control-Allow-Methods", "POST"),
            ("Access-Control-Allow-Headers", "Content-Type")
        ])

    if method != 'HEAD' or method != 'OPTIONS':
      if len(self.headers) > 0:
        self.headers.extend([('Content-Type', CONTENT_TYPE_JSON)])
      else:
        self.headers = [('Content-Type', CONTENT_TYPE_JSON)]


  def get_response(self, payload, callback):
    self.payload = payload
    self.callback = callback

    response = json.dumps(self.payload)

    self.callback(
      self.status,
      self.headers
    )
    print(self.headers)
    if payload:
      return [response.encode()]
    else:
      return []


class Ok(Response):
  status='200 Ok'


class BadRequest(Response):
  status='400 Bad Request'


class Forbidden(Response):
  status='403 Forbidden'


class NotFound(Response):
  status='404 Not Found'


class MethodNotAllowed(Response):
  status='405 Method Not Allowed'


class InternalServerError(Response):
  status='500 Internal Server Error'


class NotImplemented(Response):
  status='501 Not Implemented'


class ResponseFactory():

  def create(self, status_code, origin=None, method=None):

    if status_code == 200:
      return Ok(origin, method)
    elif status_code == 400:
      return BadRequest(origin, method)
    elif status_code == 403:
      return Forbidden(origin, method)
    elif status_code == 404:
      return NotFound(origin, method)
    elif status_code == 405:
      return MethodNotAllowed(origin, method)
    elif status_code == 500:
      return InternalServerError(origin, method)
    else:
      return NotImplemented(origin, method)
