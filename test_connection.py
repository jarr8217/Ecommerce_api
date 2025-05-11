"""
This script tests the database connection for the e-commerce API.

It initializes the Flask application, configures the database, and attempts to connect to the database engine.
If the connection is successful, a success message is printed; otherwise, an error message is displayed.
"""

from flask import Flask
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    try:
        db.engine.connect()
        print("Connection successful!")
    except Exception as e:
        print("Connection failed:", e)
