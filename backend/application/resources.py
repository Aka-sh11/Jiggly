from flask_restful import Resource, Api, reqparse, marshal_with, fields
from .models import Songs, db

api = Api(prefix='/api')

parser = reqparse.RequestParser()

songs_fields = {"id": fields.Integer, "title": fields.String, "singer": fields.String, "date": fields.String,
                "lyrics": fields.String, "genre": fields.String, "filename":fields.String,
                "user_id": fields.Integer
}

parser.add_argument("title", type=str, help="Song Title should be a string", required=True)
parser.add_argument("singer", type=str, help="Singer name should be a string", required=True) 
parser.add_argument("date", type=str, help="Date should be a string", required=True)
parser.add_argument("lyrics", type=str, help="Song Lyric should be a string", required=True)
parser.add_argument("genre", type=str, help="Song Genres should be a string", required=True)
parser.add_argument("filename", type=str, help="Filename is required and should be a string",
                    required=True)

class Song(Resource):
    @marshal_with(songs_fields)
    def get(self):
        all_songs = Songs.query.all()
        return all_songs
    
    @marshal_with(songs_fields)
    def post(self):
        args = parser.parse_args()
        songs = Songs(**args)
        db.session.add(songs)
        db.session.commit()
        return songs
    
api.add_resource(Song, '/song')