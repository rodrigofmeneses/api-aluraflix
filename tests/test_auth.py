def test_register_user(client):
    data = {
        'username': 'RFM',
        'password': '123'
    }
    response = client.post('auth/register/', json=data)
    assert response.status_code == 201
    assert b'RFM' in response.data