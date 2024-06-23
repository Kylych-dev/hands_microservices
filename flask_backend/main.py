from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mirbekov:1@db/flask_back'
CORS(app)


db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    price = db.Column(db.Float, nullable=False)

    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='unique_product_id')

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


'''
51:20
'''
