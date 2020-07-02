from flask_login import UserMixin, login_required, login_manager
from werkzeug.security import generate_password_hash
from .extensions import db, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import date, datetime


# User Account Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    address = db.Column(db.String(75), nullable=True)
    state = db.Column(db.String(75), nullable=True)
    lga = db.Column(db.String(75), nullable=True)
    phone = db.Column(db.String(100), nullable=True)
    bvn = db.Column(db.String(100), nullable=True)
    usertype = db.Column(db.String)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')

    amount_donated = db.relationship(
                                    'Donated', 
                                    foreign_keys='Donated.donated_by_id',
                                    backref='donater', 
                                    lazy=True)


    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password, method='sha256')

    

#donate model
class Donated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_amount = db.Column(db.Integer)
    #donator_name = db.Column(db.String(100), unique=False, nullable=False)
    donated_by_email = db.Column(db.String(75))
    donated_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    donator_note = db.Column(db.String, nullable=True)
    date_donated = db.Column(db.DateTime, nullable=False, default=date.today())


#shopping database
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False, unique=True)
    product_price = db.Column(db.Numeric(50,0), nullable=False)
    product_discount = db.Column(db.Integer, default=0)
    product_description = db.Column(db.String(300), nullable=False)
    product_stock = db.Column(db.Integer, nullable=False)
    product_date = db.Column(db.DateTime, nullable=False, default=date.today())

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship(
                                'Category',
                                backref='category', 
                                lazy=True)

    image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_4 = db.Column(db.String(150), nullable=False, default='image.jpg')


    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)