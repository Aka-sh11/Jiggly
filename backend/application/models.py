from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    blacklisted = db.Column(db.Boolean(), default=False)
    songs = db.relationship('Songs', backref='uploader', lazy=True)
    playlists = db.relationship('Playlist', backref='user', lazy=True)
    albums = db.relationship('Album', backref='user', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)
    roles = db.relationship('Role', secondary='roles_users', backref= db.backref('user', lazy='dynamic'))
    
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
    
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    singer = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    lyrics = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    __table_args__ = (UniqueConstraint('title', 'singer', name='unique_singer_title'),)
  
    
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
    song = db.relationship('Songs', backref='songs_in_playlist', lazy=True)
    
    
class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs_in_album = db.relationship('Songs_in_Album', backref='album', lazy=True)
    
class Songs_in_Album(db.Model):
    __tablename__ = 'songs_album'
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    song = db.relationship('Songs', backref='songs_in_album', lazy=True)
    
    
class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    song = db.relationship('Songs', backref='ratings', lazy=True)