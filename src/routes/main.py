from flask import Blueprint, render_template, request, jsonify, json, redirect, flash, url_for, Markup
from flask_login import login_required, current_user
from src.routes.auth import UpdateAccountForm
from src.extensions import db
from src.models import Donated, User
from src.models import User
import secrets
import smtplib
import os
from flask import Flask
from PIL import Image
from flask_mail import Mail
from email.message import EmailMessage

app = Flask(__name__)

main = Blueprint('main', __name__)

donate = Blueprint('donate', __name__)

shop = Blueprint('shop', __name__)


# home
@main.route('/')
@main.route('/index.html')
def index():

    # show donations function
    #username = current_user.username
    #donations = Donated.query.filter(Donated.d_amount != None).all()
    #donator_image = User.query.filter(User.image_file != None).all()
    #image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

   # context = {
    # 'donations' : donations
    # 'donator_image' : donator_image

    # }
    return render_template('index.html')

# donate


@main.route('/donate')
@main.route('/donate.html', methods=['POST', 'GET'])
# @login_required
def donate():

    return render_template('donate.html')

# donated
# @main.route('/donated', methods=['POST' , 'GET'])
# def donated():
   # if request.method == 'POST':
    # d_amount = request.form.get('donate-amount')
    # donated_by_email = request.form.get('donator-email')
    # donator_name = request.form.get('donator-name')
    # donator_note = request.form.get('donator-note')

    # new_donator = Donated (
    #     d_amount=d_amount,
    #     donated_by_email=donated_by_email,
    #     donated_by_id=current_user.id,
    #     donator_note=donator_note
    # )

    # db.session.add(new_donator)
    # db.session.commit()

    # return jsonify({'Thanks' : "Thank you " + donator_name + " for your Donation of " + d_amount + " , It means a lot to us."})

    #flash('Thank you {} for your Donations. It means a lot to us'.format(donator_name), 'success')

    # return redirect(url_for('main.index'))

    # return render_template('donated.html')


#Function for upload picture#
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, '../static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


# profile
@main.route('/profile.html', methods=['GET', 'POST'])
@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('main.profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    username = current_user.username
    firstname = current_user.firstname
    lastname = current_user.lastname
    usertype = current_user.usertype
    email = current_user.email
    amount_donated = current_user.amount_donated
    users = User.query.all()
    #donations = Donated.query.filter(Donated.d_amount != None).all()
    image_file = url_for('static', filename='profile_pics/' +
                         current_user.image_file, form=form)

    context = {
        'users': users,
        'form': form
        # 'donations' : donations
    }

    return render_template('profile.html', **context,
                           username=current_user.username,
                           firstname=current_user.firstname,
                           lastname=current_user.lastname,
                           usertype=current_user.usertype,
                           email=current_user.email,
                           image_file=image_file
                           #donations = Donated.query.filter(Donated.d_amount != None).all()
                           )

