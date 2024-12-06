from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import LoginForm, SignUpForm
from .models import Customer
from flask_login import login_user, login_required, logout_user
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():  # Validate form submission
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:
            new_customer = Customer()
            new_customer.email = email
            new_customer.username = username
            new_customer.password = password2
            
            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('Account created successfully! You can now log in.', 'success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                print(e)
                flash('An error occurred. Please try again.', 'danger')

            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''

    return render_template('signup.html', form=form) 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    print('Login route accessed')
    form = LoginForm()
    if form.validate_on_submit():  # Validate form submission
        username = form.username.data
        password = form.password.data
        # Check if user exists
        customer = Customer.query.filter_by(username=username).first()
        print(customer)
        if customer:
            if customer.verify_password(password=password):
                login_user(customer)
                print('Logged in successfully!')
                flash('Logged in successfully!', 'success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect username or password. Please try again.', 'danger')
        else:
            flash('Account does not exist. Please sign up.', 'danger')
    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('/'))


