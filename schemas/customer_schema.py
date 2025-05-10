from extensions import ma
from models.customer import Customer
from marshmallow import fields

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        include_relationships = True

        # Prevent circular recursion when serializing
        orders = fields.Nested("OrderSchema", many=True, exclude=["customer"], dump_only=True)
        