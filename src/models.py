from src import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String, nullable=False, unique=True, index=True)
    title = db.Column(db.String, nullable=False)
    reviews = db.relationship(
        'Review',
        cascade="all,delete",
        backref='product',
        lazy=True)

    def __init__(self, title, asin, reviews=None):
        self.title = title
        self.asin = asin
        if not reviews:
            self.reviews = []
        else:
            self.reviews = reviews
    
    def __repr__(self):
        return f"Product({self.asin} {self.title})"


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String, db.ForeignKey("products.id"), index=True)
    title = db.Column(db.String, nullable=False)
    review = db.Column(db.Text, nullable=False)

    def __init__(self, title, review, product_id):
        self.title = title
        self.review = review
        self.product_id = product_id
    
    def __repr__(self):
        return f"Review(product_id:{self.product_id} {self.title})"
