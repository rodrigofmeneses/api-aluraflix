import json


def test_videos_GET(client, videos):
    response = client.get('/videos/')
    assert response.status_code == 200
    assert b'Video teste 1' in response.data

def test_videos_GET_by_id(client, videos):
    response = client.get('/videos/2')
    assert response.status_code == 200
    assert b'Video teste 2' in response.data

def test_videos_POST_with_valid_json(client, videos):
    data = {
        'id': 3,
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'url teste 3'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert b'Video teste 3' in response.data
    assert b'Meu terceiro video' in response.data
    assert b'url teste 3' in response.data

def test_videos_POST_not_valid_json_missing_field(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'url': 'url teste 3'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'json body not allowed' in response.data

def test_videos_POST_not_valid_json_more_fields(client, videos):
    data = {
        'id': 3,
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'url test 3',
        'ola': 123
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'json body not allowed' in response.data

def test_videos_POST_not_valid_json_with_blank_field(client, videos):
    data = {
        'id': 3,
        'titulo': '',
        'descricao': 'Meu terceiro video',
        'url': 'url test 3'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'json body not allowed' in response.data

def test_videos_PUT_with_valid_json(client, videos):
    data = {
        'id': 1,
        'titulo': 'Video teste 1 atualizado',
        'descricao': 'Meu terceiro video atualizado',
        'url': 'url teste 1'
    }
    response = client.put('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert b'Video teste 1 atualizado' in response.data
    assert b'Meu terceiro video atualizado' in response.data
    assert b'url teste' in response.data
