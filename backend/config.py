class Config(object):
    Debug = False
    Testing = False
    
class DevelopmentConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.sqlite3"