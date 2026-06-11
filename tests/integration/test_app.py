import pytest
import os

os.environ['DB_USER'] = os.environ.get('DB_USER', 'appuser')
os.environ['DB_PASS'] = os.environ.get('DB_PASS', 'apppass')
os.environ['DB_HOST'] = os.environ.get('DB_HOST', '127.0.0.1')
os.environ['DB_NAME'] = os.environ.get('DB_NAME', 'tempconverter')

from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200

def test_conversion_post(client):
    response = client.post('/', data={'celsius': '100', 'submit': 'Convert'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'212' in response.data