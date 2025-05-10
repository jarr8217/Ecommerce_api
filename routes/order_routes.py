from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order
from schemas.order_schema import OrderSchema
from marshmallow import ValidationError

order_bp = Blueprint('order_bp', __name__, url_prefix='/orders')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# GET all orders
@order_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.jsonify(orders)

# GET one order
@order_bp.route('/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return order_schema.jsonify(order)

# POST create an order
@order_bp.route('/', methods=['POST'])
def create_order():
    try:
        new_order = order_schema.load(request.json)
        db.session.add(new_order)
        db.session.commit()
        return order_schema.jsonify(new_order), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# PUT update an order
@order_bp.route('/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    try:
        data = order_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(order, key, value)
        db.session.commit()
        return order_schema.jsonify(order)
    except ValidationError as err:
        return jsonify(err.messages), 400

# DELETE an order
@order_bp.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"})
