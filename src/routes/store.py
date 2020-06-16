from flask import Blueprint, render_template, request, redirect, url_for, Flask, flash, Markup
from flask_login import login_user, logout_user, current_user
#from flask_admin import Admin
from werkzeug.security import check_password_hash
from flask_mail import Mail
from src.extensions import db
from src.models import User, Products, Category
import smtplib
import os
from email.message import EmailMessage
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
import email_validator
from flask_wtf.file import FileField, FileAllowed
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .productform import addProducts
import secrets
from PIL import Image
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


app = Flask(__name__)

main = Blueprint('main', __name__)

store = Blueprint('store', __name__)

auth = Blueprint('auth', __name__)

donate = Blueprint('donate', __name__)



#shop
@store.route('/shop', methods=['GET', 'POST'])
@store.route('/shop.html', methods=['GET', 'POST'])
def shop():

    return render_template('shop.html')





# Add product
@store.route('/addproduct', methods=['GET', 'POST'])
@store.route('/addproduct.html', methods=['GET', 'POST'])
def addproduct():
    form = addProducts(request.form)
    categories = Category.query.all()
    if request.method == 'POST':
        product_name = form.name.data
        product_price = form.price.data
        product_discount = form.discount.data
        product_description = form.description.data
        product_stock = form.stock.data
        category = request.form.get('category')

                      
        addpro = Products(
            product_name=product_name,
            product_price=product_price,
            product_discount=product_discount,
            product_description=product_description,
            product_stock=product_stock,
            category_id=category,
           # image_1=image_1,
            #image_2=image_2,
            #image_3=image_3,
            #image_4=image_4

        )

        
        db.session.add(addpro)
        db.session.commit()

        flash(f'The product {product_name} has been added', 'success')

        #return redirect(url_for('auth.login'))

    return render_template('addproduct.html', title="Add Product", form=form, categories=categories)





