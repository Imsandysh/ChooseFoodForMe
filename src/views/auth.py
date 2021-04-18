from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # Validate and add user to database
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # If email already exists in db then it will return a user
    user = User.query.filter_by(email=email).first()
    # If a user is found redirect to signup page
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    # Create a new user with the form data
    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method='sha256')
        )

    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    print (User.query.filter_by(email="kk985@drexel.edu"))

    # Reload the page, if user does not exist or if the password is incorrect 
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # If credentials are correct, redirect to profile page
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

# login_required is used because it doesn't 
# make sense if a user logs out before logging in
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))