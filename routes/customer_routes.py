"""
This module defines the routes for handling customer-related API requests.

The routes include operations for creating, retrieving, updating, and deleting customers.
"""

from flask import Blueprint, request, jsonify
from extensions import db
from models.customer import Customer
from schemas.customer_schema import CustomerSchema
from marshmallow import ValidationError

customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# GET all customers
@customer_bp.route('/', methods=['GET'])
def get_customers():
    """
    Retrieve all customers.

    Returns:
        Response: JSON response containing a list of all customers.
    """
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)

# GET one customer
@customer_bp.route('/<int:id>', methods=['GET'])
def get_customer(id):
    """
    Retrieve a specific customer by their ID.

    Args:
        id (int): The ID of the customer to retrieve.

    Returns:
        Response: JSON response containing the customer details.
    """
    customer = Customer.query.get_or_404(id)
    return customer_schema.jsonify(customer)

# POST create customer
@customer_bp.route('/', methods=['POST'])
def create_customer():
    """
    Create a new customer.

    Returns:
        Response: JSON response containing the newly created customer or an error message.
    """
    try:
        new_customer = customer_schema.load(request.json)

        # Prevent duplicate email
        existing_customer = Customer.query.filter_by(email=new_customer.email).first()
        if existing_customer:
            return jsonify({"message": "Email already exists"}), 400
        
        
        db.session.add(new_customer)
        db.session.commit()
        return customer_schema.jsonify(new_customer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# PUT update customer
@customer_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    """
    Update an existing customer's details.

    Args:
        id (int): The ID of the customer to update.

    Returns:
        Response: JSON response containing the updated customer details or an error message.
    """
    customer = Customer.query.get_or_404(id)
    try:
        data = customer_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(customer, key, value)
        db.session.commit()
        return customer_schema.jsonify(customer)
    except ValidationError as err:
        return jsonify(err.messages), 400

# DELETE customer
@customer_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    """
    Delete a customer by their ID.

    Args:
        id (int): The ID of the customer to delete.

    Returns:
        Response: JSON response confirming the deletion of the customer.
    """
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted"})
