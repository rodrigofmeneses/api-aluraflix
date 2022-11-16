from pytest import mark

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
    assert b"user authenticate" in response.data
    assert b"token" in response.data
