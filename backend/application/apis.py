from flask import make_response, jsonify
from flask_restful import Api, NotFound, Resource, fields, marshal_with, reqparse
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash
from .models import db, Users, Role, Songs, Playlist, Songs_in_Playlist, Album, Songs_in_Album, Rating
from flask_jwt_extended import jwt_required, get_jwt_identity
from .jwt import access
import os
from datetime import datetime, timezone
from .cache import cache

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
    'role': fields.String(attribute='role.name'),
    'last_visited': fields.DateTime
}

song_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'singer': fields.String,
    'date': fields.String,
    'lyrics': fields.String,
    'genre': fields.String,
    'filename': fields.String,
    'likes': fields.Integer,
    'flags': fields.Integer,
    'user_id': fields.Integer
}

playlist_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'user_id': fields.Integer,
    'songs': fields.List(fields.Integer)
}

album_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'user_id': fields.Integer,
    'songs': fields.List(fields.Integer)
}

rating_fields = {
    'id': fields.Integer,
    'rating': fields.Integer,
    'user_id': fields.Integer,
    'song_id': fields.Integer
}

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument('username', type=str,
                         required=True, help="Username cannot be blank!")
user_parser.add_argument('password', type=str,
                         required=True, help="Password cannot be blank!")
user_parser.add_argument('email', type=str, required=True,
                         help="Email cannot be blank!")
user_parser.add_argument('role', type=str, required=True,
                         help="Role cannot be blank!")

song_parser = reqparse.RequestParser(bundle_errors=True)
song_parser.add_argument('title', type=str, required=True,
                         help="Title cannot be blank!")
song_parser.add_argument('singer', type=str, required=True,
                         help="Singer cannot be blank!")
song_parser.add_argument('date', type=str, required=True,
                         help="Date cannot be blank!")
song_parser.add_argument('lyrics', type=str, required=True,
                         help="Lyrics cannot be blank!")
song_parser.add_argument('genre', type=str, required=True,
                         help="Genre cannot be blank!")
song_parser.add_argument('filename', type=str,
                         required=True, help="Filename cannot be blank!")
song_parser.add_argument(
    'user_id', type=int, required=True, help="User ID cannot be blank!")

playlist_parser = reqparse.RequestParser(bundle_errors=True)
playlist_parser.add_argument(
    'name', type=str, required=True, help="Name cannot be blank!")
playlist_parser.add_argument(
    'user_id', type=int, required=True, help="User ID cannot be blank!")
playlist_parser.add_argument('songs', type=int, action='append')

album_parser = reqparse.RequestParser(bundle_errors=True)
album_parser.add_argument(
    'name', type=str, required=True, help="Name cannot be blank!")
album_parser.add_argument(
    'user_id', type=int, required=True, help="User ID cannot be blank!")
album_parser.add_argument('songs', type=int, action='append')

rating_parser = reqparse.RequestParser(bundle_errors=True)
rating_parser.add_argument('rating', type=int, help='Rating must be between 0 and 5',
                           required=True, choices=range(6))
rating_parser.add_argument(
    'user_id', type=int, help='User ID cannot be blank', required=True)
rating_parser.add_argument(
    'song_id', type=int, help='Song ID cannot be blank', required=True)


class UserAPI(Resource):
    @jwt_required()
    @access(['Admin', 'Creator', 'User'])
    @cache.cached(timeout=30)
    @marshal_with(user_fields)
    def get(self, user_id=None):
        if user_id:
            user = Users.query.get(user_id)
            if not user:
                raise NotFound("User not found")
            return user
        else:
            users = Users.query.all()
            return users

    @marshal_with(user_fields)
    def post(self):
        data = user_parser.parse_args()
        if Users.query.filter_by(username=data['username']).first():
            raise AlreadyExists("Username already exists")
        if Users.query.filter_by(email=data['email']).first():
            raise AlreadyExists("Email already exists")
        role = Role.query.filter_by(name=data['role']).first()
        if not role:
            raise NotFound("Role not found")
        hashed_password = generate_password_hash(data['password'])
        new_user = Users(
            username=data['username'], password=hashed_password, email=data['email'],
            role_id=role.id, last_visited=datetime.now(timezone.utc))
        db.session.add(new_user)
        db.session.commit()
        return new_user, 200

    @jwt_required()
    @marshal_with(user_fields)
    @access(['Admin', 'Creator', 'User'])
    def put(self, user_id):
        data = user_parser.parse_args()
        user = Users.query.get(user_id)
        if not user:
            raise NotFound("User not found")
        if Users.query.filter(Users.username == data['username'], Users.id != user_id).first():
            raise AlreadyExists("Username already exists")
        if Users.query.filter(Users.email == data['email'], Users.id != user_id).first():
            raise AlreadyExists("Email already exists")
        role = Role.query.filter_by(name=data['role']).first()
        if not role:
            raise NotFound("Role not found")
        user.username = data['username']
        user.password = generate_password_hash(data['password'])
        user.email = data['email']
        user.role_id = role.id
        db.session.commit()
        return user

    @jwt_required()
    @access(['Admin', 'Creator', 'User'])
    def delete(self, user_id):
        user = Users.query.get(user_id)
        if not user:
            raise NotFound("User not found")
        Rating.query.filter_by(user_id=user_id).delete()
        playlists = Playlist.query.filter_by(user_id=user_id).all()
        for playlist in playlists:
            Songs_in_Playlist.query.filter_by(
                playlist_id=playlist.id).delete()
        Playlist.query.filter_by(user_id=user_id).delete()
        albums = Album.query.filter_by(user_id=user_id).all()
        for album in albums:
            Songs_in_Album.query.filter_by(album_id=album.id).delete()
        Album.query.filter_by(user_id=user_id).delete()
        Songs.query.filter_by(user_id=user_id).delete()
        db.session.delete(user)
        db.session.commit()
        return '', 200


class SongAPI(Resource):
    @jwt_required()
    @access(['Admin', 'Creator', 'User'])
    @marshal_with(song_fields)
    def get(self, song_id=None):
        if song_id:
            song = Songs.query.get(song_id)
            if not song:
                raise NotFound("Song not found")
            return song
        else:
            songs = Songs.query.all()
            return songs

    @jwt_required()
    @access(['Creator'])
    @marshal_with(song_fields)
    def post(self):
        data = song_parser.parse_args()
        user = Users.query.get(data['user_id'])
        if not user:
            raise NotFound("User not found")
        existing_song = Songs.query.filter_by(
            title=data['title'], singer=data['singer']).first()
        if existing_song:
            raise AlreadyExists(
                "A song with this title and singer already exists")
        new_song = Songs(title=data['title'], singer=data['singer'], date=data['date'],
                         lyrics=data['lyrics'], genre=data['genre'],
                         filename=data['filename'], user_id=data['user_id'])
        db.session.add(new_song)
        db.session.commit()
        return new_song, 200

    @jwt_required()
    @marshal_with(song_fields)
    @access(['Creator'])
    def put(self, song_id):
        data = song_parser.parse_args()
        song = Songs.query.get(song_id)
        if not song:
            raise NotFound("Song not found")
        existing_song = Songs.query.filter(
            Songs.id != song_id, Songs.title == data['title'], Songs.singer == data['singer']).first()
        if existing_song:
            raise AlreadyExists(
                "A song with this title and singer already exists")
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
        # song.likes = data['likes']
        # song.flags = data['flags']
        db.session.commit()
        return song

    @jwt_required()
    @access(["Creator", "Admin"])
    def delete(self, song_id):
        song = Songs.query.get(song_id)
        if not song:
            raise NotFound("Song not found")
        Songs_in_Album.query.filter_by(
            song_id=song_id).delete()  # 1st delter it from Album
        Songs_in_Playlist.query.filter_by(
            song_id=song_id).delete()  # then delete it from Playlist
        # then delete all its reatings
        Rating.query.filter_by(song_id=song_id).delete()
        db.session.delete(song)
        db.session.commit()
        return '', 200


class PlaylistAPI(Resource):
    @jwt_required()
    @access(['User'])
    @marshal_with(playlist_fields)
    def get(self, id=None):
        if id is None:
            playlists = Playlist.query.all()
            result = []
            for playlist in playlists:
                songs = Songs_in_Playlist.query.filter_by(
                    playlist_id=playlist.id).all()
                playlist_info = {
                    "id": playlist.id,
                    "name": playlist.name,
                    "user_id": playlist.user_id,
                    "songs": [song.song_id for song in songs]
                }
                result.append(playlist_info)
            return result
        else:
            playlist = Playlist.query.get(id)
            if playlist is None:
                raise NotFound("Playlist {} doesn't exist".format(id))
            songs = Songs_in_Playlist.query.filter_by(playlist_id=id).all()
            return {"id": playlist.id, "name": playlist.name, "user_id": playlist.user_id, "songs": [song.song_id for song in songs]}

    @jwt_required()
    @access(['User'])
    @marshal_with(playlist_fields)
    def post(self):
        args = playlist_parser.parse_args()

        # Check if user_id exists
        user = Users.query.get(args['user_id'])
        if user is None:
            raise NotFound(
                "User with id {} doesn't exist".format(args['user_id']))
        # Check for unique name & user_id
        existing_playlist = Playlist.query.filter_by(
            name=args['name'], user_id=args['user_id']).first()
        if existing_playlist:
            raise AlreadyExists(
                "Playlist with this name and user_id already exists")

        new_playlist = Playlist(name=args['name'], user_id=args['user_id'])
        db.session.add(new_playlist)
        db.session.commit()

        song_ids = []
        for song_id in args['songs']:
            song = Songs.query.get(song_id)
            if song is None:
                raise NotFound("Song with id {} doesn't exist".format(song_id))
            new_song_in_playlist = Songs_in_Playlist(
                playlist_id=new_playlist.id, song_id=song_id)
            db.session.add(new_song_in_playlist)
            song_ids.append(song_id)

        new_playlist.songs = song_ids
        db.session.commit()

        return new_playlist, 200

    @jwt_required()
    @access(['User'])
    @marshal_with(playlist_fields)
    def put(self, id):
        args = playlist_parser.parse_args()
        playlist = Playlist.query.get(id)
        if playlist is None:
            raise NotFound("Playlist {} doesn't exist".format(id))

            # Check if user_id exists
        user = Users.query.get(args['user_id'])
        if user is None:
            raise NotFound(
                "User with id {} doesn't exist".format(args['user_id']))
        # Check for unique name & user_id
        existing_playlist = Playlist.query.filter_by(
            name=args['name'], user_id=args['user_id']).first()
        if existing_playlist and existing_playlist.id != id:
            raise AlreadyExists(
                "Another playlist with this name and user_id already exists")

        playlist.name = args['name']
        playlist.user_id = args['user_id']
        Songs_in_Playlist.query.filter_by(playlist_id=id).delete()
        song_ids = []
        for song_id in args['songs']:
            song = Songs.query.get(song_id)
            if song is None:
                raise NotFound("Song with id {} doesn't exist".format(song_id))
            new_song_in_playlist = Songs_in_Playlist(
                playlist_id=playlist.id, song_id=song_id)
            db.session.add(new_song_in_playlist)
            song_ids.append(song_id)
        playlist.songs = song_ids
        db.session.commit()
        return playlist, 200

    @jwt_required()
    @access(['User'])
    def delete(self, id):
        playlist = Playlist.query.get(id)
        if playlist is None:
            raise NotFound("Playlist {} doesn't exist".format(id))
        Songs_in_Playlist.query.filter_by(playlist_id=id).delete()
        db.session.delete(playlist)
        db.session.commit()
        return '', 200


class AlbumAPI(Resource):
    @jwt_required()
    @access(['Admin', 'Creator', 'User'])
    @marshal_with(album_fields)
    def get(self, id=None):
        if id is None:
            albums = Album.query.all()
            result = []
            for album in albums:
                songs = Songs_in_Album.query.filter_by(album_id=album.id).all()
                album_info = {
                    "id": album.id,
                    "name": album.name,
                    "user_id": album.user_id,
                    "songs": [song.song_id for song in songs]
                }
                result.append(album_info)
            return result
        else:
            album = Album.query.get(id)
            if album is None:
                raise NotFound("Album {} doesn't exist".format(id))
            songs = Songs_in_Album.query.filter_by(album_id=id).all()
            return {"id": album.id, "name": album.name, "user_id": album.user_id, "songs": [song.song_id for song in songs]}

    @jwt_required()
    @access(['Creator'])
    @marshal_with(album_fields)
    def post(self):
        args = album_parser.parse_args()

        # Check if user_id exists
        user = Users.query.get(args['user_id'])
        if user is None:
            raise NotFound(
                "User with id {} doesn't exist".format(args['user_id']))

        # Check for unique name & user_id
        existing_album = Album.query.filter_by(
            name=args['name'], user_id=args['user_id']).first()
        if existing_album:
            raise AlreadyExists(
                "Album with this name and user_id already exists")

        song_ids = []
        for song_id in args['songs']:
            song = Songs.query.get(song_id)
            if song is None:
                raise NotFound("Song with id {} doesn't exist".format(song_id))
            song_ids.append(song_id)

        new_album = Album(name=args['name'], user_id=args['user_id'])
        db.session.add(new_album)
        db.session.commit()

        for song_id in song_ids:
            new_song_in_album = Songs_in_Album(
                album_id=new_album.id, song_id=song_id)
            db.session.add(new_song_in_album)
            db.session.commit()
        new_album.songs = song_ids
        return new_album, 200

    @jwt_required()
    @access(['Creator'])
    @marshal_with(album_fields)
    def put(self, id):
        args = album_parser.parse_args()
        album = Album.query.get(id)
        if album is None:
            raise NotFound("Album {} doesn't exist".format(id))

            # Check if user_id exists
        user = Users.query.get(args['user_id'])
        if user is None:
            raise NotFound(
                "User with id {} doesn't exist".format(args['user_id']))
        # Check for unique name
        existing_album = Album.query.filter_by(name=args['name']).first()
        if existing_album and existing_album.id != id:
            raise AlreadyExists("Another Album with this name already exists")

        album.name = args['name']
        album.user_id = args['user_id']
        Songs_in_Album.query.filter_by(album_id=id).delete()
        song_ids = []
        for song_id in args['songs']:
            song = Songs.query.get(song_id)
            if song is None:
                raise NotFound("Song with id {} doesn't exist".format(song_id))
            new_song_in_album = Songs_in_Album(
                album_id=album.id, song_id=song_id)
            db.session.add(new_song_in_album)
            song_ids.append(song_id)
        album.songs = song_ids
        db.session.commit()
        return album, 200

    @jwt_required()
    @access(['Admin', 'Creator'])
    def delete(self, id):
        album = Album.query.get(id)
        if album is None:
            raise NotFound("Album {} doesn't exist".format(id))
        Songs_in_Album.query.filter_by(album_id=id).delete()
        db.session.delete(album)
        db.session.commit()
        return '', 200


class RatingAPI(Resource):
    @jwt_required()
    @access(['Admin', 'Creator', 'User'])
    @marshal_with(rating_fields)
    def get(self, song_id=None, user_id=None):
        if song_id is None or user_id is None:
            ratings = Rating.query.all()
            return ratings
        else:
            rating = Rating.query.filter_by(
                song_id=song_id, user_id=user_id).first()
            if not rating:
                raise NotFound("Rating not found")
            return rating

    @jwt_required()
    @access(['Admin', 'Creator', 'User'])
    @marshal_with(rating_fields)
    def post(self):
        args = rating_parser.parse_args()
        user = Users.query.get(args['user_id'])
        song = Songs.query.get(args['song_id'])
        if not user:
            raise BadRequest("User ID does not exist")
        if not song:
            raise BadRequest("Song ID does not exist")
        new_rating = Rating(
            rating=args['rating'], user_id=args['user_id'], song_id=args['song_id'])
        db.session.add(new_rating)
        db.session.commit()
        return new_rating, 200

    @jwt_required()
    @access(['User', 'Creator'])
    @marshal_with(rating_fields)
    def put(self, rating_id):
        args = rating_parser.parse_args()
        rating = Rating.query.get(rating_id)
        if not rating:
            raise NotFound("Rating not found")
        rating.rating = args['rating']
        rating.user_id = args['user_id']
        rating.song_id = args['song_id']
        db.session.commit()
        return rating

    @jwt_required()
    @access(['User'])
    def delete(self, rating_id):
        rating = Rating.query.get(rating_id)
        if not rating:
            raise NotFound("Rating not found")
        db.session.delete(rating)
        db.session.commit()
        return '', 200


api.add_resource(UserAPI, '/user/<int:user_id>', '/user')
api.add_resource(SongAPI, '/song/<int:song_id>', '/song')
api.add_resource(PlaylistAPI, '/playlist/<int:id>', '/playlist')
api.add_resource(AlbumAPI, '/album/<int:id>', '/album')
api.add_resource(RatingAPI, '/ratings/<int:rating_id>',
                 '/ratings', '/ratings/<int:song_id>/<int:user_id>')
