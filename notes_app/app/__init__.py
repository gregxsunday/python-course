from app.core.auth import mod as auth_blueprint
from app.core.notes import mod as notes_blueprint
from app.core.views import mod as core
from app.database.models import User, Note
from app.extensions import db
import secrets
from flask_login import LoginManager
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import uuid
from os import environ
from flask_wtf.csrf import CSRFProtect


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    CSRFProtect(app)

    # db = SQLAlchemy(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # session
    SESSION_TYPE = 'sqlalchemy'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():
        @app.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404

        @login_manager.user_loader
        def load_user(user_id):
            # since the user_id is just the primary key of our user table, use it in the query for the user
            return User.query.get(int(user_id))

        db.create_all()

        # create users upon first run
        if len(User.query.all()) == 0:
            login = 'gniedziela'
            password = secrets.token_urlsafe(16)
            description = environ.get('FLAG2', r'flag{testflag2}')

            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(
                login=login,
                password=generate_password_hash(password),
                uuid=str(uuid.uuid4()),
                description=description
            )
            db.session.add(new_user)

            for i in range(1, 30):
                name = f'Notatka {i}'
                if i == 13:
                    content = environ.get('FLAG1', r'flag{testflag1}')
                elif i == 29:
                    content = 'Idziesz w dobrym kierunku.'
                else:
                    content = f'Zawartość {i}'
                note = Note(name=name, content=content, user=new_user)
                db.session.add(note)

            # add the new user to the database
            db.session.commit()

        app.register_blueprint(core)
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(notes_blueprint)
    return app
