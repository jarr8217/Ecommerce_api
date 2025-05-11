# E-commerce REST API

This is a modular e-commerce RESTful API built with Flask, SQLAlchemy, and Marshmallow. It supports managing customers, products, and orders with proper database relationships and JSON serialization.

---

## Features

- Full CRUD operations for:
  - Customers
  - Products
  - Orders
- Many-to-Many relationship between Orders and Products
- One-to-Many relationship between Customers and Orders
- JSON serialization with Marshmallow
- Validation and error handling
- Tested with Postman
- Modular structure with Blueprints and separate schema/model layers

---

## Technologies Used

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow
- MySQL
- Postman (for API testing)

---

## Project Structure

```
e_commerce_api/
├── app.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── order.py
│   ├── product.py
│   └── order_product.py
├── schemas/
│   ├── customer_schema.py
│   ├── order_schema.py
│   └── product_schema.py
├── routes/
│   ├── customer_routes.py
│   ├── order_routes.py
│   └── product_routes.py
├── extensions.py
├── requirements.txt
└── README.md
```

---

## Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ecommerce_api.git
cd ecommerce_api
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
# On Windows use: 
.venv\Scripts\activate
# On Mac use:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up database URI in `config.py`
```python
# config.py
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root1234!@localhost/ecommerce_api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 5. Create the database and tables
In MySQL Workbench:
```sql
CREATE DATABASE ecommerce_api;
```

Then run in Python:
```python
from app import db
db.create_all()
```

### 6. Run the app
```bash
flask run
```

---

## Postman Collection

A complete Postman collection with all API endpoints can be exported or recreated based on:
- `/customers/`
- `/products/`
- `/orders/`

Includes actions like adding products to orders, getting customer order history, etc.

---

## Example Endpoints

| Method | Endpoint                                   | Description                  |
|--------|--------------------------------------------|------------------------------|
| GET    | `/customers/`                              | Get all customers            |
| POST   | `/products/`                               | Create a new product         |
| POST   | `/orders/`                                 | Create a new order           |
| POST   | `/orders/<order_id>/products/<product_id>` | Add product to order         |
| GET    | `/orders/<order_id>/products`              | Get all products in an order |
| DELETE | `/orders/<order_id>`                       | Delete an order              |

---

## Author

**Jose Refoyo-Ron**  
[LinkedIn](www.linkedin.com/in/jose-refoyo-ron-660a52321)  
[GitHub](https://github.com/jarr8217)

