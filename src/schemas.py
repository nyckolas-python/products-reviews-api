from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.models import Product, Review


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True
        fields = ('id', 'asin', 'title', 'reviews')
    reviews = Nested('ReviewSchema', many=True, default=[], exclude=('products',))


class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True
        # fields = ('id', 'product_id', 'title', 'review')
    products = Nested('ProductSchema', exclude=('reviews',))
