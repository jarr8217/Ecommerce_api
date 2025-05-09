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
