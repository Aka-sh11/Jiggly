from flask import request, make_response, jsonify
from flask_restful import Api, NotFound, Resource, fields, marshal_with, reqparse
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash
from .models import db, Users, Role ,Songs, Playlist, Songs_in_Playlist, Album, Songs_in_Album, Rating


api = Api(prefix='/api')

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

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'blacklisted': fields.Boolean,
    'role': fields.String(attribute='role.name')
}

song_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'singer': fields.String,
    'date': fields.String,
    'lyrics': fields.String,
    'genre': fields.String,
    'filename': fields.String,
    'user_id': fields.Integer
}

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
user_parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
user_parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
user_parser.add_argument('role', type=str, required=True, help="Role cannot be blank!")

song_parser = reqparse.RequestParser(bundle_errors=True)
song_parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
song_parser.add_argument('singer', type=str, required=True, help="Singer cannot be blank!")
song_parser.add_argument('date', type=str, required=True, help="Date cannot be blank!")
song_parser.add_argument('lyrics', type=str, required=True, help="Lyrics cannot be blank!")
song_parser.add_argument('genre', type=str, required=True, help="Genre cannot be blank!")
song_parser.add_argument('filename', type=str, required=True, help="Filename cannot be blank!")
song_parser.add_argument('user_id', type=int, required=True, help="User ID cannot be blank!")


class UserAPI(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = Users.query.get(user_id)
        if not user:
            raise NotFound("User not found")
        return user

    @marshal_with(user_fields)
    def post(self):
        data = user_parser.parse_args()
        if Users.query.filter_by(username=data['username']).first():
            raise AlreadyExists("Username already exists")
        role = Role.query.filter_by(name=data['role']).first()
        if not role:
            raise NotFound("Role not found")
        hashed_password = generate_password_hash(data['password'])
        new_user = Users(username=data['username'], password=hashed_password, email=data['email'], role_id=role.id)
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201

    @marshal_with(user_fields)
    def put(self, user_id):
        data = user_parser.parse_args()
        user = Users.query.get(user_id)
        if not user:
            raise NotFound("User not found")
        role = Role.query.filter_by(name=data['role']).first()
        if not role:
            raise NotFound("Role not found")
        user.username = data['username']
        user.password = generate_password_hash(data['password'])
        user.email = data['email']
        user.role_id = role.id
        db.session.commit()
        return user

    def delete(self, user_id):
        user = Users.query.get(user_id)
        if not user:
            raise NotFound("User not found")
        db.session.delete(user)
        db.session.commit()
        return '', 204



class SongAPI(Resource):
    @marshal_with(song_fields)
    def get(self, song_id):
        song = Songs.query.get(song_id)
        if not song:
            raise NotFound("Song not found")
        return song

    @marshal_with(song_fields)
    def post(self):
        data = song_parser.parse_args()
        user = Users.query.get(data['user_id'])
        if not user:
            raise NotFound("User not found")
        existing_song = Songs.query.filter_by(title=data['title'], singer=data['singer']).first()
        if existing_song:
            raise AlreadyExists("A song with this title and singer already exists")
        new_song = Songs(title=data['title'], singer=data['singer'], date=data['date'], 
                        lyrics=data['lyrics'], genre=data['genre'],
                        filename=data['filename'], user_id=data['user_id'])
        db.session.add(new_song)
        db.session.commit()
        return new_song, 201

    @marshal_with(song_fields)
    def put(self, song_id):
        data = song_parser.parse_args()
        song = Songs.query.get(song_id)
        if not song:
            raise NotFound("Song not found")
        existing_song = Songs.query.filter(Songs.id != song_id, Songs.title == data['title'], Songs.singer == data['singer']).first()
        if existing_song:
            raise AlreadyExists("A song with this title and singer already exists")
        user = Users.query.get(data['user_id'])
        if not user:
            raise NotFound("User not found")
        song.title = data['title']
        song.singer = data['singer']
        song.date = data['date']
        song.lyrics = data['lyrics']
        song.genre = data['genre']
        song.filename = data['filename']
        song.user_id = data['user_id']
        db.session.commit()
        return song


    def delete(self, song_id):
        song = Songs.query.get(song_id)
        if not song:
            raise NotFound("Song not found")
        db.session.delete(song)
        db.session.commit()
        return '', 204


api.add_resource(UserAPI, '/user/<int:user_id>','/user')
api.add_resource(SongAPI, '/song/<int:song_id>', '/song')
