from src.models import Product, Review

class ProductService:
    @staticmethod
    def fetch_all_product(session):
        return session.query(Product)
    
    @classmethod
    def fetch_product_by_id(cls, session, id):
        return cls.fetch_all_product(session).filter_by(
            id=id
        )

class ReviewService:
    @staticmethod
    def fetch_all_reviews(session):
        return session.query(Review)
    
    @classmethod
    def fetch_reviews_by_product_id(cls, session, product_id):
        return cls.fetch_all_reviews(session).filter_by(
            product_id=product_id
        )
        