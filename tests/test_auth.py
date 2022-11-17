from pytest import mark

from app.models import User

def test_register_user(client, users):
    data = {"username": "RFM", "password": "123"}
    response = client.post("auth/register/", json=data)
    assert response.status_code == 201
    assert b"RFM" in response.data

def test_register_existent_username(client, users):
    data = {"username": "rodrigo", "password": "abcd"}
    client.post("auth/register/", json=data)
    response = client.post("auth/register/", json=data)
    assert response.status_code == 400
    assert b"Username must be unique" in response.data

def test_authenticate_user(client, users):
    data = {"username": "rodrigo", "password": "1234"}
    response = client.post("auth/", json=data)
    assert response.status_code == 200
    assert b"user rodrigo authenticated" in response.data
    assert b"token" in response.data

def test_encode_auth_token(client, users):
    user = users[0]
    auth_token = user.encode_auth_token()
    assert len(auth_token) > 30

def test_decode_auth_token(client, users):
    user = users[0]
    auth_token = user.encode_auth_token()
    assert len(auth_token) > 30
    assert User.decode_auth_token(auth_token) == user.id

def test_acess_protected_route_with_unauthorized_user(client, videos, users):
    response = client.get('videos/')
    assert response.status_code == 401