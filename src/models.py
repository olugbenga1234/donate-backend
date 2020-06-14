from flask_login import UserMixin, login_required, login_manager
from werkzeug.security import generate_password_hash
from .extensions import db, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import date


# register model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    address = db.Column(db.String(75), nullable=False, server_default='None', default='None')
    state = db.Column(db.String(75), nullable=False, server_default='None', default='None')
    lga = db.Column(db.String(75), nullable=False, server_default='None', default='None')
    phone = db.Column(db.Integer, default='000')
    bvn = db.Column(db.Integer, default='000')
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
    donator_note = db.Column(db.String, nullable=False, default='comment', server_default='comment')
    date_donated = db.Column(db.DateTime, nullable=False, default=date.today())
