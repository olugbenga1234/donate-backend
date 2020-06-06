from flask import Blueprint, render_template

from src.extensions import db
from src.models import Donated
from src.models import User


main = Blueprint('main', __name__)

donate = Blueprint('donate', __name__)

@main.route('/')
@main.route('/index.html')
def index():
    return render_template('index.html')


@main.route('/donate')
@main.route('/donate.html')
def donate():
    return render_template('donate.html')

@main.route('/shop')
@main.route('/shop.html')
def shop():
    return render_template('shop.html')

@main.route('/users')
@main.route('/users.html')
#@login_required
def users():
    #if not current_user.admin
        #return redirect(url_for('main.index'))

   # users = User.query.filter_by(admin=False).all()
    users = User.query.all()

    context = {
        'users' : users
    }
    
    return render_template('users.html', **context)