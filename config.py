import os
import pathlib


BASE_DIR = pathlib.Path(__file__).parent


class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-know'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        str(BASE_DIR / "data" / "flask_db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopementConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300


class ProductionConfig(BaseConfig):
    DEBUG = False
