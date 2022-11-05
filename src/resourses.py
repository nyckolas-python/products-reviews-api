from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload, selectinload

from src import db, cache
from src.models import Product, Review
from src.schemas import ProductSchema, ReviewSchema
from src.services import ProductService, ReviewService


class ProductApi(Resource):
    product_schema = ProductSchema()
    reviews_schema = ReviewSchema()

    # @cache.cached()
    def get(self, id=None):
        product = ProductService.fetch_product_by_id(db.session, id).options(
            joinedload(Product.reviews)
        ).first()
        if not product:
            return {'message': 'there is no product with this id'}, 404
        page = request.args.get('page', 0, type=int)
        if 0 < page <= len(product.reviews):
            reviews = ReviewService \
                .fetch_reviews_by_product_id(db.session, id) \
                .paginate(page=page, per_page=1)

            product.reviews.clear()
            product.reviews.extend(reviews.items)
        elif page > len(product.reviews):
            return {'message': 'there is no page with this number'}, 404

        return self.product_schema.dump(product), 200

    def post(self):
        return {'message': 'method not allowed'}, 405

    # @cache.cached()
    def put(self, id):
        product = ProductService.fetch_product_by_id(db.session, id).options(
            joinedload(Product.reviews)
        )
        if not product:
            return {'message': 'there is no product with this id'}, 404
        try:
            review = self.reviews_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        try:
            db.session.add(review)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return {'message': str(e)}, 409

        return self.product_schema.dump(product), 201

    def delete(self):
        return {'message': 'method not allowed'}, 405
