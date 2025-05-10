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
    products = Product.query.all()
    return jsonify(products_schema.dump(products))

# GET one product
@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product_schema.dump(product))

# POST create product
@product_bp.route('/', methods=['POST'])
def create_product():
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
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})

