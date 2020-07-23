from flask import Blueprint, render_template, request, redirect, url_for, Flask, flash, Markup
from flask_login import login_user, logout_user, current_user, login_required
#from flask_admin_1 import admin_1
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
from .productform import addProducts

app = Flask(__name__)

main = Blueprint('main', __name__)

store = Blueprint('store', __name__)

auth = Blueprint('auth', __name__)

donate = Blueprint('donate', __name__)

admin_1 = Blueprint('admin_1_1', __name__)



#function for admin register
@admin_1.route('/r41234', methods=['GET', 'POST'])
@admin_1.route('/r41234.html', methods=['GET', 'POST'])
def registeradmin():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        email = request.form.get('email')
        unhashed_password = request.form.get('password')
        usertype = 'admin'

       
#check if username exists
        checkusername = User.query.filter_by(username=username).first()

        if checkusername:
            flash(Markup(' Username already exists. Already have an account?<a href="login.html" style="color: yellow; font-weight: 900;"> Login In</a>'), 'error')
            return redirect(url_for('auth.register'))

#check if email already exists
        checkuseremail = User.query.filter_by(email=email).first()

        if checkuseremail:
            flash(Markup(' Email already exists. Already have an account?<a href="login.html" style="color: yellow; font-weight: 500;"> Login In</a>'), 'error')
            return redirect(url_for('auth.register'))


        new_user = User(
                    lastname=lastname,
                    firstname=firstname,
                    username=username,
                    unhashed_password=unhashed_password,
                    email=email,                  
                    usertype=usertype
                    )
                    
        db.session.add(new_user)
        db.session.commit()

        flash('Registered successfully', 'success')
        return redirect(url_for('auth.login'))

    return render_template('admin-register.html')


# # admin_1
# @admin_1.route('/admin_1', methods=['GET', 'POST'])
# @admin_1.route('/admin_1.html', methods=['GET', 'POST'])
# # @login_required
# def admin_1istrator():

#     #display_products = Products.query.all()

#     # context = {
#     # 'display_products' : display_products

#     # }

#     return render_template('admin_1.html')  # **context)


# # edit products
# @admin_1.route('/del-product', methods=['GET', 'POST'])
# @admin_1.route('/del-product.html', methods=['GET', 'POST'])
# # @login_required
# def del_products():

#     displays = Products.query.all()

#     return render_template('admin_1_display_products.html', displays=displays)


# # Add category
# @admin_1.route('/addcat', methods=['GET', 'POST'])
# @admin_1.route('/addcat.html', methods=['GET', 'POST'])
# # @login_required
# def addcat():
#     if request.method == 'POST':
#         getcat = request.form.get('category')
#         cat = Category(
#             name=getcat
#         )

#         db.session.add(cat)
#         db.session.commit()

#         return redirect(url_for('admin_1.addcat'))

#     return render_template('addcat.html', title="Add Category")


# #display categories
# @admin_1.route('/cat', methods=['GET', 'POST'])
# @admin_1.route('/cat.html', methods=['GET', 'POST'])
# # @login_required
# def cat():
#     if request.method == 'POST':
#         getcat = request.form.get('category')
#         cat = Category(
#             name=getcat
#         )

#         db.session.add(cat)
#         db.session.commit()

#         return redirect(url_for('store.addcat'))

#     return render_template('admin_1_cat.html', title="Add Category")



# # edit categories
# @admin_1.route('/editcat/<int:id>', methods=['GET', 'POST'])
# @admin_1.route('/editcat.html/<int:id>', methods=['GET', 'POST'])
# # @login_required
# def editcat(id):
#     updatecat = Category.query.get_or_404(id)
#     getcat = request.form.get('category')

#     if request.method == 'POST':
#         updatecat.name = getcat

#         flash(f'Category Updated', 'success')
#         db.session.commit
#         return redirect(url_for('admin_1.cat'))
#     return render_template('admin_1_editcat.html', title="Edit Category", updatecat=updatecat)

# #update products
# @admin_1.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
# def updateproduct(id):
#     form = addProducts(request.form)   
#     categories = Category.query.all()
#     display = Products.query.get_or_404(id)
#     category = request.form.get('category')
#     if request.method == 'POST':
#         display.product_name = form.name.data
#         display.product_price = form.price.data
#         display.product_discount = form.discount.data
#         display.product_stock = form.stock.data
#         display.product_description = form.descriptikon.data
#         display.category_id = category
#         db.session.commit()
#         flash('Product Updated', 'success')
#         return redirect(url_for('admin_1.del_products'))
        

#     form.name.data = display.product_name
#     form.price.data = display.product_price
#     form.discount.data = display.product_discount
#     form.stock.data = display.product_stock
#     # form.description.data = display.product_description


#     return render_template('updateproduct.html', form=form, display=display, categories=categories)

#delete products
#@admin_1.route('/deleteproduct/<int:id>', methods=['GET', 'POST'])
#def deleteproducts(id):

    #display = Products.query.get_or_404(id)
    #if request.method == 'POST':
    #    db.session.delete(display)
    #    db.session.commit()
    #    flash(f'Product {display.product_name} has been deleted','success')
    #    return redirect(url_for('admin_1.del_products'))
    #flash('can not delete the product ', 'error')
    #return redirect(url_for('admin_1.del_products'))
    