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

def test_categorias_POST_with_invalid_json_missing_field(client, categorias):
    data = {
        'titulo': 'Terror',
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Missing data for required field.' in response.data

def test_categorias_POST_with_invalid_json_more_fields(client, categorias):
    data = {
        'titulo': 'Video teste 3',
        'cor': 'black',
        'ola': 123
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Unknown field.' in response.data

def test_categorias_POST_with_invalid_json_blank_fields(client, categorias):
    data = {
        'titulo': '',
        'cor': ''
    }
    response = client.post('/categorias/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank' in response.data

def test_categorias_PUT_with_valid_json(client, categorias):
    data = {
        'titulo': 'Titulo atualizado',
        'cor': 'Cor atualizada'
    }
    response = client.put('/categorias/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert b'Titulo atualizado' in response.data
    assert b'Cor atualizada' in response.data

def test_categorias_PUT_with_invalid_json_invalid_id(client, categorias):
    data = {
        'titulo': 'Terror',
        'cor': 'black'
    }
    response = client.put('/categorias/15', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 404
    assert b'categoria not found' in response.data

def test_categorias_PUT_with_invalid_json_missing_fields(client, categorias):
    data = {
        'titulo': 'Terror',
    }
    response = client.put('/categorias/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Missing data for required field.' in response.data
    
def test_categorias_PUT_with_invalid_json_more_fields(client, categorias):
    data = {
        'titulo': 'Terror',
        'cor': 'black',
        'ola': 123
    }
    response = client.put('/categorias/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Unknown field' in response.data
    
def test_categorias_PUT_with_invalid_json_blank_fields(client, categorias):
    data = {
        'titulo': '',
        'cor': 'black'
    }
    response = client.put('/categorias/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank.' in response.data

def test_categorias_PATCH_with_valid_json(client, categorias):
    data = {
        'cor': 'green'
    }
    response = client.patch('/categorias/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert b'"id": 1' in response.data
    assert b'green' in response.data

def test_categorias_PATCH_with_invalid_json_blank_fields(client, categorias):
    data = {
        'cor': '',
    }
    response = client.patch('/categorias/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert b'Must not blank' in response.data