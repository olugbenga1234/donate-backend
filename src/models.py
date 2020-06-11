from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from .extensions import db



# this is the model for the database

# register model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    password = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(75))
    state = db.Column(db.String(75))
    lga = db.Column(db.String(75))
    phone = db.Column(db.Integer, unique=True)
    bvn = db.Column(db.Integer)
    usertype = db.Column(db.String)

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
    donator_note = db.Column(db.String)
