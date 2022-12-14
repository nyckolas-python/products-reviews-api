import config

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy, record_queries
from flask_caching import Cache


app = Flask(__name__)
app.config.from_object(config.ProductionConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
cache = Cache(app)
cache.init_app(app)

app.debug = True


def sql_debug(response):
    queries = list(record_queries.get_recorded_queries())
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration

    print('=' * 80)
    print(' SQL Queries - {0} Queries Executed in {1}ms'.format(
        len(queries), round(total_duration * 1000, 2)))
    print('=' * 80)

    return response


app.after_request(sql_debug)

from src import routes, models
