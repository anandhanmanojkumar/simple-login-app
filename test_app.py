import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    response = client.get('/')
    assert b"Welcome" in response.data  # Change this if your homepage uses different text
