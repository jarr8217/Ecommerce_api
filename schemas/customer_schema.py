from extensions import ma
from models.customer import Customer
from marshmallow import fields, validate

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
        error_messages={
            "required": "Customer name is required.",
            "validator_failed": "Name must be between 1 and 100 characters."
        }
    )

    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
            "invalid": "Invalid email format."
        }
    )

    address = fields.String(
        allow_none=True,
        validate=validate.Length(max=255),
        error_messages={
            "validator_failed": "Address must be 255 characters or fewer."
        }
    )

    # Nested orders (output only)
    orders = fields.Nested("OrderSchema", many=True, exclude=["customer"], dump_only=True)

    class Meta:
        model = Customer
        load_instance = True
        include_relationships = True
        include_fk = True
