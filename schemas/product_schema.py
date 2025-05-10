from extensions import ma, db
from models.product import Product
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = False
        sqla_session = db.session 

    # Include order details in output
    # Avoid circular recursion when serializing
    # dump_only=True ensures that this field is not included when deserializing
    orders = fields.Nested("OrderSchema", exclude=["products"], many=True, dump_only=True)