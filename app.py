"""
This module initializes and runs the Flask application for the e-commerce API.

The application is configured with database and serialization extensions, and it registers routes for handling API requests.
"""

from flask import Flask
from config import Config
from extensions import db, ma
from routes import register_routes
from models.customer import Customer
from models.order import Order

def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    register_routes(app)

    # Create tables explicitly
    with app.app_context():
        db.create_all()
        print("Tables created successfully!")

    return app

if __name__ == '__main__':
    """
    Entry point for running the Flask application.
    """
    app = create_app()
    app.run(debug=True)
