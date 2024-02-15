from flask import make_response
from werkzeug.exceptions import HTTPException

# Validations
class BaseHTTPError(HTTPException):
    def __init__(self, status_code, message):
        self.response = make_response(message, status_code)

class NotFoundError(BaseHTTPError):
    def __init__(self, message):
        super().__init__(404, message)

class UnauthorizedError(BaseHTTPError):
    def __init__(self, message):
        super().__init__(409, message)
        
class ConflictError(BaseHTTPError):
    def __init__(self, message):
        super().__init__(415, message)