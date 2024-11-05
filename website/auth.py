from flask import Blueprint, render_template
from wtforms import form
from  .forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__)


@auth.route('/sign-up')
def sign_up():
    form = SignUpForm()
    return render_template('sign-up.html', form=form)
    return "This is the sign up page"

@auth.route('/login')
def login():
    return "This is the login page"


