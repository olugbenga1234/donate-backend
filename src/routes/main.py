from flask import Blueprint, render_template

from src.extensions import db
from src.models import Donated

app.config['SECRET KEY'] = 'shsshsjfhf38384844dff8f8fd8dv8vf888f8f8ff8'

main = Blueprint('main', __name__)

donate = Blueprint('donate', __name__)

@main.route('/')
@main.route('/index.html')
def index():
    return render_template('index.html')


@main.route('/donate.html')
def donate():
    return render_template('donate.html')

@main.route('/shop.html')
def shop():
    return render_template('shop.html')
