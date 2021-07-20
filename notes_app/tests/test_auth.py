import pytest
from flask import url_for
from hashlib import sha256
import json
import secrets

from app import app, db
from app.database.models import User

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_user_in_database(client):
    user = User.query.filter_by(login='gniedziela').first()
    assert user
    assert 'flag{' in user.description


def test_signup(client):
    login = secrets.token_urlsafe(16)
    password = secrets.token_urlsafe(16)
    description = secrets.token_urlsafe(32)

    data = {
        'login': login,
        'password': password,
        'description': description
    }

    resp = client.post('/signup', data=data)
    assert resp.status_code == 302
    assert  '/login' in resp.location

    user = User.query.filter_by(login=login).first()
    assert user
    assert description == user.description

def test_duplicate_signup(client):
    login = 'gniedziela'
    password = secrets.token_urlsafe(16)

    data = {
        'login': login,
        'password': password
    }

    resp = client.post('/signup', data=data, follow_redirects=True)
    user = User.query.filter_by(login='gniedziela').first()

    assert user.uuid.encode('utf8') in resp.data

def test_signup_and_login(client):
    login = secrets.token_urlsafe(16)
    password = secrets.token_urlsafe(16)

    data = {
        'login': login,
        'password': password
    }

    resp = client.post('/signup', data=data)
    assert resp.status_code == 302
    assert  '/login' in resp.location

    user = User.query.filter_by(login=login).first()
    assert user

    data = {
        'login': login,
        'password': password
    }
    resp = client.post('/login', data=data)
    assert resp.status_code == 302
    assert '/profile' in resp.location
    
def test_getting_flag(client):
    login = 'gniedziela'
    password = secrets.token_urlsafe(16)

    data = {
        'login': login,
        'password': password
    }

    resp = client.post('/signup', data=data, follow_redirects=True)
    user = User.query.filter_by(login='gniedziela').first()

    assert user.uuid.encode('utf8') in resp.data
    gniedziela_uuid = user.uuid

    login = secrets.token_urlsafe(16)
    password = secrets.token_urlsafe(16)

    data = {
        'login': login,
        'password': password
    }

    resp = client.post('/signup', data=data)
    assert resp.status_code == 302
    assert  '/login' in resp.location

    user = User.query.filter_by(login=login).first()
    assert user

    data = {
        'login': login,
        'password': password
    }
    resp = client.post('/login', data=data)
    assert resp.status_code == 302
    assert '/profile' in resp.location

    resp = client.get(f'/profile/{gniedziela_uuid}')
    assert b'flag{' in resp.data