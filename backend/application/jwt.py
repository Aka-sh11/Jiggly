from flask import jsonify, request
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_current_user, get_jwt
from .models import Users
    

def get_user_by_identity(identity):
    return Users.query.filter_by(id=identity).first()

def access(roles: []):  # type: ignore
    '''RBAC + blacklisted decorator'''
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            verify_jwt_in_request()
            identity = get_current_user()
            current_user = get_user_by_identity(identity)
            if current_user.role not in roles or current_user.blacklisted:
                return jsonify(msg="unauthorized access"), 403
            return f(*args, **kwargs)
        return decorator_function
    return decorator



