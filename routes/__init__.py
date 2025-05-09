from .customer_routes import customer_bp

def register_routes(app):
    app.register_blueprint(customer_bp)
