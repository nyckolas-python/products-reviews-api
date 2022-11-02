from wsgi import app
from flask import request, redirect, jsonify


@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/products/<int:id>', methods=['GET', 'POST'])
def products(id: int):
    return f"Hello Product {id}"