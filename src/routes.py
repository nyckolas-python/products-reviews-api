from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload, selectinload

from src import api, db
from src.models import Product, Review
from src.schemas import ProductSchema, ReviewSchema


class ProductApi(Resource):
    product_schema = ProductSchema()
    reviews_schema = ReviewSchema()
    
    def get(self, id=None):
        product = db.session.query(Product).options(
            joinedload(Product.reviews)
        ).filter_by(id=id).one_or_none()
        if not product:
            return {'message': 'there is no product with this id'}, 404
        page = request.args.get('page', 0, type=int)
        if 0 < page <= len(product.reviews):
            reviews = db.session.query(Review)\
                .filter_by(product_id=id)\
                .paginate(page=page, per_page=1)

            product.reviews.clear()
            product.reviews.extend(reviews.items)
        elif page > len(product.reviews):
            return {'message': 'there is no page with this number'}, 404

        return self.product_schema.dump(product), 200

    def post(self):
        return {'message': 'method not allowed'}, 405

    def put(self, id):
        product = db.session.query(Product).options(
            joinedload(Product.reviews)
        ).filter_by(id=id).one_or_none()
        if not product:
            return {'message': 'there is no product with this id'}, 404
        try:
            review = self.reviews_schema.load(request.json, session=db.session)
            print(review)
            db.session.add(review)
            db.session.commit()
        except ValidationError as e:
            return {'message': str(e)}, 400
        
        return self.product_schema.dump(product), 201

    def delete(self):
        return {'message': 'method not allowed'}, 405


api.add_resource(ProductApi, '/product/<int:id>', strict_slashes=False)
