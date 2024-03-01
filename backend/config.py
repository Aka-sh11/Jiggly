from datetime import datetime,timedelta

class Config(object):
    Debug = False
    Testing = False
    
class DevelopmentConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.sqlite3"
    JWT_SECRET_KEY= "SECRET_KEY"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=10)