from flask import Blueprint, render_template, request, jsonify, json, redirect, flash, url_for
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
@login_required
def donate():
    
    return render_template('donate.html')

#donated
@main.route('/donated', methods=['POST' , 'GET'])
def donated():
    if request.method == 'POST':
        d_amount = request.form.get('donate-amount')
        donated_by_email = request.form.get('donator-email')
        donator_name = request.form.get('donator-name')
        donator_note = request.form.get('donator-note')

        new_donator = Donated (
            d_amount=d_amount,
            donated_by_email=donated_by_email,
            donated_by_id=current_user.id
        )
                                
        db.session.add(new_donator)
        db.session.commit()

        return jsonify({'Thanks' : "Thank you " + donator_name + " for your Donation of " + d_amount + " , It means a lot to us."})

        #flash('Thank you {} for your Donations. It means a lot to us'.format(donator_name), 'success')

        #return redirect(url_for('main.index'))

    return render_template('donated.html')


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
    #firstname = current_user.firstname 
    #users = User.query.all()
  
    #context = {
    #    'users' : users,
    #}
    
    #return render_template('users.html', **context,  username=current_user.username, firstname=current_user.firstname, amount=current_user.d_amount)
    donations = Donated.query.filter(Donated.d_amount != None).all()

    context = {
        'donations' : donations
    }
    
    return render_template('users.html', **context, username=current_user.username,)

#profile
@main.route('/profile')
@login_required
def profile():
    username = current_user.username
    firstname = current_user.firstname 
    lastname = current_user.lastname
    usertype = current_user.usertype
    email = current_user.email
    amount_donated = current_user.amount_donated
    users = User.query.all()
    #donations = Donated.query.filter(Donated.d_amount != None).all()  

    context = {
        'users' : users,
        #'donations' : donations
    }
    

    return render_template('profile.html', **context, \
        username=current_user.username,\
        firstname=current_user.firstname,\
        lastname=current_user.lastname, \
        usertype=current_user.usertype,\
        email=current_user.email
        #donations = Donated.query.filter(Donated.d_amount != None).all()
        )
