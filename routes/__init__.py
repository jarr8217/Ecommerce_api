"""
This module initializes and registers all route blueprints for the e-commerce API.

The blueprints include routes for customers, orders, and products.
"""

from .customer_routes import customer_bp
from .order_routes import order_bp
from .product_routes import product_bp

def register_routes(app):
    app.register_blueprint(customer_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(product_bp)
