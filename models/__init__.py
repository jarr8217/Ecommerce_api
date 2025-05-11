"""
This module imports all models for the e-commerce API.

The models include Customer, Order, Product, and the association table order_products.
"""

from .customer import Customer
from .order import Order
from .product import Product
from .order_product import order_products
