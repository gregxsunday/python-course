import pytest
from flask import url_for
from hashlib import sha256
import json
import secrets

from app import app, db
from app.database.models import User, Note

@pytest.fixture
def client():
    with app.test_client() as client:
        login = secrets.token_urlsafe(16)
        password = secrets.token_urlsafe(16)

        data = {
            'login': login,
            'password': password
        }

        resp = client.post('/signup', data=data)

        data = {
            'login': login,
            'password': password
        }
        resp = client.post('/login', data=data)
        yield client



def test_creating_notes(client):
    user = User.query.filter_by(login='gniedziela').first()
    assert user
    note = Note(name='Testnote', content='Test Note Content', user=user)
    db.session.add(note)
    db.session.commit()

    assert Note.query.filter_by(name='Testnote').first()

def test_adding_note(client):
    data = {
        'name': 'test name',
        'content': 'test content'
    }

    resp = client.post('/notes/', data=data, follow_redirects=True)
    assert b'test name' in resp.data

def test_getting_flag(client):
    resp = client.get('/notes/13')
    assert b'flag{' in resp.data

