from extensions import ma
from models.order import Order
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True  # Needed to include customer_id

    # Include customer details in output
    customer = fields.Nested("CustomerSchema", exclude=["orders"], dump_only=True)
    products = fields.Nested("ProductSchema", exclude=["orders"], many=True, dump_only=True)
