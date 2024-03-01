from flask import jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_current_user, get_jwt
    
def access(roles:[]): # type: ignore
    '''RBAC decorator'''
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            verify_jwt_in_request()
            current_user = get_current_user()
            if current_user.role not in roles:
                return jsonify(msg="unauthorized access"), 403
            return f(*args, **kwargs)
        return decorator_function
    return decorator