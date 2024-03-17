from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify

class BadRequest(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 400)


class AlreadyExists(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 409)


class AuthenticationError(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 401)


class AuthorizationError(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 403)


class NotFound(HTTPException):
    def __init__(self, message):
        # self.response = make_response(message, 404)
        self.response = make_response(jsonify(message), 404)


class InternalError(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 500)
