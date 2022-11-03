import csv

from src import db, app
from src.models import Product, Review
from config import BASE_DIR


def save_products_to_db():
    """
    The function open ./data/Products.csv,
    reads the file line by line .csv file,
    checks if there is an record in the database,
    if there is no duplicate, it adds an record of Product.
    """
    path_to_csv_files = str(BASE_DIR / "data" / "Products.csv")
    try:
        with open(path_to_csv_files, 'r') as input_csv:
            csvreader = csv.reader(input_csv)
            # advance past the header
            header = next(csvreader)
            print(header)
            with app.app_context():
                for row in csvreader:
                    # filtering existing
                    exist = db.session.query(
                        Product.query.filter(
                            Product.asin==row[1]
                            ).exists()
                        ).scalar()
                    if not exist:
                        product = Product(
                            title=row[0],
                            asin=row[1]
                            )
                        db.session.add(product)
                        print(f"Product {row[1]} - was populated...")
                    else:
                        print(f"Product {row[1]} - has already existed...")

                # db.session.query(Review).delete()
                db.session.commit()
                db.session.close()
                print('Products successfully loaded!')
    except Exception as error:
        print(f"{error}")

def save_reviews_to_db():
    """
    The function open ./data/Reviews.csv,
    reads the file line by line .csv file,
    checks if there is an record in the database,
    if there is no duplicate, it adds an record of Review.
    """
    path_to_csv_files = str(BASE_DIR / "data" / "Reviews.csv")
    try:
        with open(path_to_csv_files, 'r') as input_csv:
            csvreader = csv.reader(input_csv)
            # Advance past the header
            header = next(csvreader)
            print(header)
            with app.app_context():
                for row in csvreader:
                    # filtering existing
                    product_reviews = db.session.query(
                        Product
                            ).filter(
                                Product.asin==row[0]
                                ).one().reviews
                    exist = [True if (review.title==row[1] and review.review==row[2])
                             else False
                             for review in product_reviews]
                    # print(not any(exist))
                    # cheking has already existed
                    if not any(exist) or exist == []:
                        product_id = db.session.query(
                            Product
                            ).filter(
                                Product.asin==row[0]
                                ).one().id
                        review = Review(
                            product_id=product_id,
                            title=row[1],
                            review=row[2]
                            )
                        db.session.add(review)
                        print(f"Rewiew for {row[0]} - was populated...")
                    else:
                        print(f"Rewiew for {row[0]} - has already existed...")

                # db.session.query(Review).delete()
                db.session.commit()
                db.session.close()
                print('Reviews successfully loaded!')
    except Exception as error:
        print(f"{error}")

if __name__ == '__main__':
    print('Load data from csv to db...')
    save_products_to_db()
    save_reviews_to_db()
