from flask import current_app as app, jsonify, make_response, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, unset_jwt_cookies
from .jwt import access
from .models import Users, Songs, Album
from werkzeug.security import check_password_hash
from sqlalchemy import or_

@app.get('/')
def home():
    return "hello world"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    user = Users.query.filter_by(username=username).first()
    if not user:
        return make_response('User Not Found', 404)
    if not check_password_hash(user.password, password):
        return make_response('Invalid Password', 400)

    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    if not access_token or not refresh_token:
        return make_response("Error Generating Token", 500)
    else:
        return jsonify(user=user.to_dict(), access_token=access_token)


@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"message": "Logout Successful"})
    unset_jwt_cookies(response)
    return response, 200


@app.route('/search', methods=['POST'])
def search():
    query = request.json['search']
    song_results = Songs.query.filter(
        or_(Songs.title.contains(query), Songs.singer.contains(
            query), Songs.genre.contains(query))
    ).all()
    album_results = Album.query.filter(
        or_(Album.name.contains(query))
    ).all()
    # Convert the results to JSON and return them
    return jsonify(song_results=song_results, album_results=album_results)
