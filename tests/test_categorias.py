import json
from pytest import mark


def test_categorias_GET(client, categorias):
    response = client.get('/categorias/')
    assert response.status_code == 200
    assert b'LIVRE' in response.data
    assert b'Categoria teste 1' in response.data

def test_categorias_GET_by_id(client, categorias):
    response = client.get('/categorias/2')
    assert response.status_code == 200
    assert b'Categoria teste 1' in response.data

def test_categorias_GET_by_id_with_invalid_id(client, categorias):
    response = client.get('/categorias/15')
    assert response.status_code == 404
    assert b'categoria not found' in response.data

def test_categorias_POST_with_valid_json(client, categorias):
    data = {
        'titulo': 'Terror',
        'cor': 'black'
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert b'Terror' in response.data
    assert b'black' in response.data

def test_categorias_POST_with_not_valid_json_missing_field(client, categorias):
    data = {
        'titulo': 'Terror',
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Missing data for required field.' in response.data

def test_categorias_POST_with_not_valid_json_more_fields(client, categorias):
    data = {
        'titulo': 'Video teste 3',
        'cor': 'black',
        'ola': 123
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Unknown field.' in response.data

def test_categorias_POST_with_not_valid_json_blank_fields(client, categorias):
    data = {
        'titulo': '',
        'cor': ''
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank' in response.data