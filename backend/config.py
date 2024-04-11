from datetime import datetime,timedelta

class Config(object):
    Debug = False
    Testing = False
    
class DevelopmentConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///jiggly.sqlite3"
    JWT_SECRET_KEY= "SECRET_KEY"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=10)
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 3