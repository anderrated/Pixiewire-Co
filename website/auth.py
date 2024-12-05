from flask import Blueprint, render_template, request, flash, redirect, url_for
from wtforms import form
from  .forms import LoginForm, SignUpForm
from .models import Customer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():  # Validate form submission
        email = form.email.data
        username = form.username.data
        password = form.password1.data

        # Check if user already exists
        existing_user = Customer.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already registered.', 'danger')
            return redirect(url_for('auth.sign_up'))

        # Create a new user
        new_user = Customer(email=email, username=username, password=generate_password_hash(password))
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(e)
            flash('An error occurred. Please try again.', 'danger')   
    return render_template('signup.html', form=form) 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Validate form submission
        email = form.email.data
        password = form.password.data

        # Check if user exists
        user = Customer.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('views.home'))  # Replace with your main page route
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('views.home'))


