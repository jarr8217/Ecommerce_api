"""
This module initializes the extensions used in the e-commerce application.

Extensions:
    - SQLAlchemy: For database interactions.
    - Marshmallow: For serialization and deserialization of data.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


'''
This module initializes the extensions used in the application.
- SQLAlchemy: for database interactions
- Marshmallow: for serialization and deserialization of data
'''

db = SQLAlchemy()
ma = Marshmallow()

