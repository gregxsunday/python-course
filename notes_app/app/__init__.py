from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from os import environ
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('app.config')
CsrfProtect(app)

# db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# session
SESSION_TYPE = 'sqlalchemy'


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

from app.core.views import mod as core
app.register_blueprint(core)

from app.core.auth import mod as auth_blueprint
app.register_blueprint(auth_blueprint)

from app.core.notes import mod as notes_blueprint
app.register_blueprint(notes_blueprint)

from app.database.models import *
db.create_all()

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

import secrets
from hashlib import sha256

# create users upon first run
if len(User.query.all()) == 0:
  login = 'gniedziela'
  password = secrets.token_urlsafe(16)
  description = environ.get('FLAG2', r'flag{testflag2}')

  # create a new user with the form data. Hash the password so the plaintext version isn't saved.
  new_user = User(
    login=login, 
    password=generate_password_hash(password, method='sha256'), 
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



# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)

