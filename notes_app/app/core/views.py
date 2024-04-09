from flask import Blueprint, render_template, redirect, url_for
from app.database.models import User
from sqlalchemy import exc
from hashlib import sha256
from flask_login import login_required, current_user

mod = Blueprint('core', __name__)


@mod.route('/')
def index():
    return (render_template('core/index.html', nav='index'))


@mod.route('/profile')
@login_required
def profile():
    return redirect(url_for('core.get_profile', uuid=current_user.uuid))


@mod.route('/profile/<uuid>')
@login_required
def get_profile(uuid):
    user = User.query.filter_by(uuid=uuid).first_or_404()
    # FIX: if user == current_user
    return render_template('core/profile.html', nav='profile', login=user.login, description=user.description)
