from extensions import db



class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(225), nullable=False, unique=True)
    address = db.Column(db.String(225))

    orders = db.relationship('Order', back_populates='customer', cascade='all, delete', lazy='select')