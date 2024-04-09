from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
    abort, jsonify, make_response
from app.database.models import User
from sqlalchemy import exc
from hashlib import sha256
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from flask_login import login_user
from app.extensions import db

mod = Blueprint('auth', __name__)


@mod.route('/login')
def login():
    return render_template('auth/login.html', nav='login')


@mod.route('/signup')
def signup():
    return render_template('auth/signup.html', nav='signup')


@mod.route('/signup', methods=['POST'])
def signup_post():
    login = request.form.get('login')
    password = request.form.get('password')
    desc = request.form.get('description')

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(login=login).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash(f'Login zajęty przez użytkownika {user.uuid}')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(
        login=login,
        password=generate_password_hash(password),
        uuid=str(uuid.uuid4()),
        description=desc
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@mod.route('/login', methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(login=login).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Niewłaściwe dane logowania. Spróbuj ponownie.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('core.profile'))
