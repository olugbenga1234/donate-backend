from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField, BooleanField, TextAreaField, validators, DecimalField

class addProducts(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    stock = IntegerField('Stock', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    description = TextAreaField('Description', [validators.DataRequired()])

    #image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    #image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    #image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    #image_4 = FileField('Image 4', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])