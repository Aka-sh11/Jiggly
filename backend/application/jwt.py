from flask import jsonify, request
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_current_user, get_jwt_identity
from .models import Users
    

def get_user_by_identity(identity):
    return Users.query.filter_by(id=identity).first()


def access(roles: []):  # type: ignore
    '''RBAC + blacklisted decorator'''
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            verify_jwt_in_request()
            user = get_jwt_identity()
            current_user = Users.query.filter_by(id=user).first()
            if current_user.role.name not in roles or current_user.blacklisted:
                return {"message":"Unauthorized Access"}, 403
            return f(*args, **kwargs)
        return decorator_function
    return decorator



