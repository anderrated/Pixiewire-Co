from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, length

class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')