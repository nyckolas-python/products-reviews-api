from flask import request
from flask_restful import Resource

from src import api, db


class Home(Resource):
    def get(self):
        return {'message': 'OK'}


api.add_resource(Home, '/', strict_slashes=False)