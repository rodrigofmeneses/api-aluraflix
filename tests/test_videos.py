import json
from urllib import response
from pytest import mark


def test_videos_GET(client, videos):
    response = client.get('/videos/')
    assert response.status_code == 200
    assert b'Video teste 1' in response.data

def test_videos_GET_by_id(client, videos):
    response = client.get('/videos/2')
    assert response.status_code == 200
    assert b'Video teste 2' in response.data

def test_videos_GET_by_id_with_invalid_id(client, videos):
    response = client.get('/videos/15')
    assert response.status_code == 404
    assert b'video not found' in response.data

def test_videos_POST_with_valid_json(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'https://www.google.com/'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert b'Video teste 3' in response.data
    assert b'Meu terceiro video' in response.data
    assert b'https://www.google.com/' in response.data
    assert b'"categoria_id": 1' in response.data

def test_videos_POST_with_valid_json_and_category_id(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'https://www.google.com/',
        'categoria_id': 2
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert b'Video teste 3' in response.data
    assert b'Meu terceiro video' in response.data
    assert b'"categoria_id": 2' in response.data

def test_videos_POST_with_not_valid_json_missing_field(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'url': 'https://www.google.com/'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Missing data for required field.' in response.data

def test_videos_POST_with_not_valid_json_more_fields(client, videos):
    data = {
        'titulo': 'Video teste 3',
        'descricao': 'Meu terceiro video',
        'url': 'https://www.google.com/',
        'ola': 123
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Unknown field.' in response.data

def test_videos_POST_with_not_valid_json_blank_fields(client, videos):
    data = {
        'titulo': '',
        'descricao': 'Meu terceiro video',
        'url': 'https://www.google.com/'
    }
    response = client.post('/videos/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank' in response.data

def test_videos_PUT_with_valid_json(client, videos):
    data = {
        'titulo': 'Video teste 1 atualizado',
        'descricao': 'Meu terceiro video atualizado',
        'url': 'https://www.google.com/'
    }
    response = client.put('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert b'Video teste 1 atualizado' in response.data
    assert b'Meu terceiro video atualizado' in response.data
    assert b'https://www.google.com/' in response.data

def test_videos_PUT_with_not_valid_json_missing_fields(client, videos):
    data = {
        'descricao': 'Meu terceiro video atualizado',
        'url': 'https://www.google.com/'
    }
    response = client.put('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Missing data for required field.' in response.data
    
def test_videos_PUT_with_not_valid_json_more_fields(client, videos):
    data = {
        'descricao': 'Meu terceiro video atualizado',
        'url': 'https://www.google.com/',
        'ola': 123
    }
    response = client.put('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Unknown field' in response.data
    
def test_videos_PUT_with_not_valid_json_blank_fields(client, videos):
    data = {
        'descricao': '',
        'url': 'https://www.google.com/'
    }
    response = client.put('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank.' in response.data
    
def test_videos_PATCH_with_valid_json(client, videos):
    data = {
        'titulo': 'Video teste 1 atualizado'
    }
    response = client.patch('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert b'"id": 1' in response.data
    assert b'Video teste 1 atualizado' in response.data
    assert b'Meu primeiro video' in response.data
    assert b'https://www.google.com/' in response.data

def test_videos_PATCH_with_not_valid_json_blank_fields(client, videos):
    data = {
        'titulo': ''
    }
    response = client.patch('/videos/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank' in response.data

def test_videos_DELETE(client, videos):
    response = client.delete('/videos/1')
    assert response.status_code == 200
    assert b'successfully deleted' in response.data

def test_videos_DELETE_wrong_id(client, videos):
    response = client.delete('/videos/4')
    assert response.status_code == 404
    assert b'fail to delete, video not found' in response.data