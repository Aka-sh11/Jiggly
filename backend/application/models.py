from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from datetime import datetime, timezone

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    blacklisted = db.Column(db.Boolean(), default=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    songs = db.relationship('Songs', backref='uploader', lazy=True)
    playlists = db.relationship('Playlist', backref='user', lazy=True)
    albums = db.relationship('Album', backref='creator', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)
    last_visited = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    # roles = db.relationship('Role', backref='user', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'blacklisted': self.blacklisted,
            # 'role_id': self.role_id,
            'role': self.role.name,
            'last_visited': self.last_visited.strftime('%Y-%m-%d %H:%M:%S')
        }
    
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    users = db.relationship('Users', backref='role', lazy=True)
    
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    singer = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    lyrics = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, default=0)
    flags = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    __table_args__ = (UniqueConstraint('title', 'singer', name='unique_singer_title'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'singer': self.singer,
            'date': self.date,
            'lyrics': self.lyrics,
            'genre': self.genre,
            'filename': self.filename,
            'user_id': self.user_id,
            'likes': self.likes,
            'flags': self.flags
        }
  
    
class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs_in_playlist = db.relationship('Songs_in_Playlist', backref='playlist', lazy=True)
    __table_args__ = (UniqueConstraint('name', 'user_id', name='playlist_user'),)
   
    
class Songs_in_Playlist(db.Model):
    __tablename__ = 'songs_playlist'
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    song = db.relationship('Songs', backref='songs_playlist', lazy=True)
    
    
class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs_in_album = db.relationship('Songs_in_Album', backref='albums', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }
    
class Songs_in_Album(db.Model):
    __tablename__ = 'songs_album'
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    song = db.relationship('Songs', backref='songs_album', lazy=True)
    
    
class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    song = db.relationship('Songs', backref='ratings', lazy=True)
    