import os
import pathlib


BASE_DIR = pathlib.Path(__file__).parent


class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-know'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        str(BASE_DIR / "data" / "flask_db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300


class DevelopementConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    DB_HOST = os.environ.get('DB_HOST', 'postgres')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'flask_api_dev')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'flask_api_dev')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'pass')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + \
        POSTGRES_USER + ':' + POSTGRES_PASSWORD + \
        '@' + DB_HOST + '/' +POSTGRES_DB
