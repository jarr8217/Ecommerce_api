from flask import Flask
from config import Config
from extensions import db, ma
from routes import register_routes
from models.customer import Customer
from models.order import Order

def create_app():
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
    app = create_app()
    app.run(debug=True)
