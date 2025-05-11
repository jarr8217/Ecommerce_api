"""
This module defines the schema for serializing and deserializing Order objects.

The OrderSchema class uses Marshmallow to validate and serialize order data, including relationships with customers and products.
"""

from extensions import ma
from models.order import Order
from marshmallow import fields, validate

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True  # Allows customer_id input

    # Validate status field to accept only specific values
    status = fields.String(
        required=True,
        validate=validate.OneOf(["pending", "in transit", "shipped", "delivered", "cancelled"]),
        error_messages={
            "required": "Status is required.",
            "validator_failed": "Invalid status. Must be one of: pending, in transit, shipped, delivered, cancelled."
        }
    )

    customer_id = fields.Integer(required=True, error_messages={"required": "Customer ID is required."})

    # Output only
    customer = fields.Nested("CustomerSchema", exclude=["orders"], dump_only=True)
    products = fields.Nested("ProductSchema", exclude=["orders"], many=True, dump_only=True)
