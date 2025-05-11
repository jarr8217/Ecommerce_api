from extensions import db
from models.product import Product
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate

class ProductSchema(SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))
    description = fields.String(allow_none=True)

    class Meta:
        model = Product
        load_instance = False
        sqla_session = db.session 

    # Include order details in output
    # Avoid circular recursion when serializing
    # dump_only=True ensures that this field is not included when deserializing
    orders = fields.Nested("OrderSchema", exclude=["products"], many=True, dump_only=True)