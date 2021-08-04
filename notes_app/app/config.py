import os
import secrets

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = secrets.token_urlsafe(32)
# SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = False
WTF_CSRF_ENABLED = False
CSRF_SESSION_KEY = secrets.token_urlsafe(32)
