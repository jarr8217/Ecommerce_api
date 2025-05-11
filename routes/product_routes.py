"""
This module defines the routes for handling product-related API requests.

The routes include operations for creating, retrieving, updating, and deleting products.
"""

from flask import Blueprint, request, jsonify
from extensions import db
from models.product import Product
from schemas.product_schema import ProductSchema
from marshmallow import ValidationError

product_bp = Blueprint('product_bp', __name__, url_prefix='/products')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# GET all products
@product_bp.route('/', methods=['GET'])
def get_all_products():
    """
    Retrieve all products.

    Returns:
        Response: JSON response containing a list of all products.
    """
    products = Product.query.all()
    return jsonify(products_schema.dump(products))

# GET one product
@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    """
    Retrieve a specific product by its ID.

    Args:
        id (int): The ID of the product to retrieve.

    Returns:
        Response: JSON response containing the product details.
    """
    product = Product.query.get_or_404(id)
    return jsonify(product_schema.dump(product))

# POST create product
@product_bp.route('/', methods=['POST'])
def create_product():
    """
    Create a new product.

    Parses the JSON request body to create a new product and saves it to the database.

    Returns:
        Response: JSON response containing the created product details and a 201 status code.
    """
    try:
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
# PUT update product
@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    """
    Update an existing product.

    Args:
        id (int): The ID of the product to update.

    Parses the JSON request body to update the product details.

    Returns:
        Response: JSON response containing the updated product details.
    """
    product = Product.query.get_or_404(id)
    try:
        data = product_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return jsonify(product_schema.dump(product))
    except ValidationError as err:
        return jsonify(err.messages), 400
    
# DELETE product
@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    """
    Delete a product.

    Args:
        id (int): The ID of the product to delete.

    Deletes the product from the database.

    Returns:
        Response: JSON response containing a message indicating successful deletion.
    """
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})

