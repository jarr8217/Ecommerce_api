"""
This module defines the routes for handling order-related API requests.

The routes include operations for creating, retrieving, updating, and deleting orders,
as well as managing the relationships between orders, products, and customers.
"""

from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order
from models.product import Product
from models.customer import Customer
from schemas.order_schema import OrderSchema
from schemas.product_schema import ProductSchema
from marshmallow import ValidationError

order_bp = Blueprint('order_bp', __name__, url_prefix='/orders')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# GET all orders
@order_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders)), 200

# GET one order
@order_bp.route('/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order_schema.dump(order)), 200

# POST create an order
@order_bp.route('/', methods=['POST'])
def create_order():
    try:
        new_order = order_schema.load(request.json)
        
        # Check if customer exists
        customer = Customer.query.get(new_order.customer_id)
        if not customer:
            return jsonify({"message": "Customer not found"}), 404

        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# PUT update an order
@order_bp.route('/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    try:
        data = request.json
        order_schema.load(data, partial=True)  # Validate only
        for key, value in data.items():
            setattr(order, key, value)
        db.session.commit()
        return jsonify(order_schema.dump(order)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

# DELETE an order
@order_bp.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"}), 200

# Add product to an order
@order_bp.route('/<int:order_id>/products/<int:product_id>', methods=['POST'])
def add_product_to_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)

    if product in order.products:
        return jsonify({"message": "Product already in order"}), 400

    order.products.append(product)
    db.session.commit()
    return jsonify(order_schema.dump(order)), 201

# Remove product from an order
@order_bp.route('/<int:order_id>/products/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)

    if product not in order.products:
        return jsonify({"message": "Product not in order"}), 400

    order.products.remove(product)
    db.session.commit()
    return jsonify(order_schema.dump(order)), 200

# Get all orders for a customer
@order_bp.route('/customer/<int:customer_id>/orders', methods=['GET'])
def get_orders_by_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(orders_schema.dump(customer.orders)), 200

# Get all products in an order
@order_bp.route('/<int:order_id>/products', methods=['GET'])
def get_products_in_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(products_schema.dump(order.products)), 200
