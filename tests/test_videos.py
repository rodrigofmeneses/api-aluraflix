import json


def test_videos_GET(client, videos):
    response = client.get('/videos/')
    assert response.status_code == 200
    assert b'Video teste 1' in response.data

def test_videos_GET_by_id(client, videos):
    response = client.get('/videos/2')
    assert response.status_code == 200
    assert b'Video teste 2' in response.data

def test_videos_POST_validate(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'url teste'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert b'Video teste 3' in response.data
    assert b'Meu terceiro video' in response.data
    assert b'url teste' in response.data

def test_videos_POST_not_validate_missing_field(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'url': 'url teste'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'something wrong' in response.data

def test_videos_POST_not_validate_duplicated_url(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'https://www.youtube.com/watch?v=xFrGuyw1V8s'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'something wrong' in response.data

def test_videos_PUT_with_valid_json(client, videos):
    data = {
        'titulo': 'Video teste 1 atualizado',
        'descricao': 'Meu terceiro video atualizado',
        'url': 'https://www.youtube.com/watch?v=xFrGuyw1V8s'
    }
    response = client.put('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert b'Video teste 1 atualizado' in response.data
    assert b'Meu terceiro video atualizado' in response.data
    assert b'https://www.youtube.com/watch?v=xFrGuyw1V8s' in response.data