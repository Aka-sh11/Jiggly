from flask_restful import Resource, Api, reqparse, marshal_with, fields
from ..models import Songs, db
from .validations import *


songApi = Api()

parser = reqparse.RequestParser()

songs_fields = {"id": fields.Integer, "title": fields.String, "singer": fields.String, 
                "date": fields.String, "lyrics": fields.String, "genre": fields.String,
                "filename":fields.String, "user_id": fields.Integer
                }

parser.add_argument("title", type=str, help="Song Title should be a string", required=True)
parser.add_argument("singer", type=str, help="Singer name should be a string", required=True) 
parser.add_argument("date", type=str, help="Date should be a string", required=True)
parser.add_argument("lyrics", type=str, help="Song Lyric should be a string", required=True)
parser.add_argument("genre", type=str, help="Song Genres should be a string", required=True)
parser.add_argument("filename", type=str, help="Filename is required and should be a string",
                    required=True)

class ViewSong(Resource):
    @marshal_with(songs_fields)
    def get(self, song_id):
        song = Songs.query.get(song_id)
        if song:
            return song, 200
        else:
            raise NotFoundError(message="Song not found")
 
class AddSong(Resource):    
    @marshal_with(songs_fields)
    def post(self):
        args = parser.parse_args()
        song = Songs(**args)
        # Get the data from request body
        # title = args.get("title", None)
        # singer = args.get("singer", None)
        # date = args.get("date", None)
        # lyrics = args.get("lyrics", None)
        # genre =args.get("genre", None)
        # filename = args.get("filename", None)
        # user_id = args.get("user_id", None)
        #         # check if a song with same title & singer already exits
        # existing_song = Songs.query.filter_by(title=title, singer=singer).first() 
        # if existing_song:
        #     raise ConflictError(message="Song already exist")
        
        # song = Songs(title=title,singer=singer,date=date,lyrics=lyrics,genre=genre,
        #              filename=filename,user_id=user_id)  
        db.session.add(song)
        db.session.commit()
        return song
    
# Add resources to the API
songApi.add_resource(ViewSong, '/song/<int:song_id>')
songApi.add_resource(AddSong, '/song')