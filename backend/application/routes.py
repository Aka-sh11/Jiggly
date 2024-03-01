from flask import current_app as app, jsonify, make_response, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, unset_jwt_cookies
from .jwt import access
from .models import Users
from werkzeug.security import check_password_hash

@app.get('/')
def home():
    return "hello world"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    user = Users.query.filter_by(username=username).first()
    if not user:
        return make_response('user not found', 404)
    if not check_password_hash(user.password, password):
        return make_response('invalid password', 400)

    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    if not access_token or  not refresh_token:
        return make_response("error generating Token", 500)
    else:
        return jsonify(user=user.to_dict(), access_token=access_token)
    
@app.route('/logout',methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"message":"Logout Successful"})
    unset_jwt_cookies(response)
    return response, 200