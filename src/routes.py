from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Product, Review


class ProductApi(Resource):
    def get(self, id=None):
        product = db.session.query(Product).filter_by(id=id).first()
        if not product:
            return {'message': 'there is no product with this id'}, 404
        return {'message': 'OK'}

    def post(self):
        return {'message': 'method not allowed'}, 405

    def put(self, id):
        review_json = request.json
        if not review_json:
            return {'message': 'Wrong data'}, 400
        try:
            review = Review(
                product_id=id,
                title=review_json['title'],
                review=review_json['review']
            )
            db.session.add(review)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully', 'id': review.id}, 201

    def delete(self, uuid):
        return {'message': 'method not allowed'}, 405


api.add_resource(ProductApi, '/product/<int:id>', strict_slashes=False)