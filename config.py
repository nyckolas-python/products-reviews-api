import os


app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'

class DevelopementConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False