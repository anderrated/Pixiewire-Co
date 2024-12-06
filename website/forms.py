from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# User authentication forms

class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6), EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
