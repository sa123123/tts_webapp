from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email

class SignupForm(FlaskForm):
    firstname=StringField('First Name',validators=[DataRequired(),Length(min=2,max=20)])
    lastname=StringField('Last Name',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email address",validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    number=StringField('Phone Number',validators=[DataRequired()])
    signup=SubmitField('SIGN UP!')
class LoginForm(FlaskForm):
    email=StringField('Email address',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    login=SubmitField('LOGIN')