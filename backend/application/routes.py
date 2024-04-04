from flask import current_app as app, jsonify, make_response, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, unset_jwt_cookies, get_jwt_identity
from .jwt import access
from .models import Users, Songs, Album, db
from werkzeug.security import check_password_hash
from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from .jwt import access


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


@app.route('/fetchuserinfo', methods=['GET'])
@jwt_required()
def fetch_user_info():
    current_user = get_jwt_identity()
    user = Users.query.filter_by(id=current_user).first()
    if not user:
        return make_response('User Not Found', 404)
    return jsonify(user=user.to_dict()), 200


@app.route('/search/', methods=['GET'])
# @jwt_required()
def search():
    query = request.args.get('search')
    song_results = Songs.query.filter(
        or_(Songs.title.ilike(f'%{query}%'))
    ).all()
    return jsonify(song_results=[song.to_dict() for song in song_results])


@app.route('/creatorSongs', methods=['GET'])
@jwt_required()
def get_songs():
    songs = db.session.query(Songs).options(
        joinedload(Songs.uploader).joinedload(Users.role)).all()
    creator_songs = [
        song.to_dict() for song in songs if song.uploader.role.name == 'Creator']
    return jsonify(creator_songs)


@app.route('/creatorAlbums', methods=['GET'])
@jwt_required()
def get_albumss():
    albums = db.session.query(Album).options(
        joinedload(Album.creator).joinedload(Users.role)).all()
    creator_albums = [
        album.to_dict() for album in albums if album.creator.role.name == 'Creator']
    return jsonify(creator_albums)


@app.route('/blacklist/<int:id>', methods=['PUT'])
@jwt_required()
def blacklist_user(id):
    user = Users.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    if 'blacklisted' in request.json:
        user.blacklisted = request.json['blacklisted']
        db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200
