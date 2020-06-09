from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from src.extensions import db
from src.models import Donated
from src.models import User


main = Blueprint('main', __name__)

donate = Blueprint('donate', __name__)

#home
@main.route('/')
@main.route('/index.html')
def index():
    return render_template('index.html')

#donate
@main.route('/donate')
@main.route('/donate.html', methods=['POST','GET'])
def donate():

    if request.method == 'POST':
        donate_amount = request.form['donate-amount']
        donated_by_email = request.form['donator-email']
        donator_username = request.form['donator-username']

        if donate_amount and donated_by_email:
            return jsonify({'Thank you for donation' : donated_by_email})

        new_donator = donate(
                    donate_amount=donate_amount,
                    donated_by_email=donated_by_email
                    )

        db.session.add(new_donator)
        db.session.commit()

    
    return render_template('donate.html')

#shop
@main.route('/shop')
@main.route('/shop.html')
def shop():
    return render_template('shop.html')

#users
@main.route('/users')
@main.route('/users.html')
@login_required
def users():
    username = current_user.username
    users = User.query.all()

    context = {
        'users' : users
    }
    
    return render_template('users.html', **context,  username=current_user.username)