"""
This module defines the Order model for the e-commerce application.

The Order model represents a customer's order, including details such as
the order date, status, and relationships with customers, products, and
order-product associations.
"""

from extensions import db
from datetime import date
from models.order_product import order_products  


class Order(db.Model):
    """
    Represents an order in the e-commerce system.

    Attributes:
        id (int): The primary key of the order.
        order_date (date): The date the order was placed. Defaults to today's date.
        status (str): The status of the order (e.g., "pending"). Defaults to "pending".
        customer_id (int): The foreign key referencing the associated customer.
        customer (Customer): The customer who placed the order.
        order_products (list[OrderProduct]): The list of order-product associations.
        products (list[Product]): The list of products associated with the order.
    """
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, default=date.today)
    status = db.Column(db.String(50), default="pending")
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
   
   # One-to-Many relationship with Customer
    customer = db.relationship('Customer', back_populates='orders')
    # Many-to-Many relationship with Product
    products = db.relationship('Product', secondary=order_products, back_populates='orders')
