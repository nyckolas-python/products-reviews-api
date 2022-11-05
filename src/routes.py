from src import api
from src.resourses import ProductApi


api.add_resource(ProductApi, '/api/v1/products/<int:id>', strict_slashes=False)
