import os 
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY")

    _database_url = os.getenv('DATABASE_URL')

    if os.path.exists("/.dockerenv") and _database_url:
        _database_url = _database_url.replace("localhost", "db").replace("127.0.0.1", "db")

    SQLALCHEMY_DATABASE_URI = _database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_URL = os.getenv("REDIS_URL")
    JWT_SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)