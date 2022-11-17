from urllib import response
from pytest import mark


def test_videos_GET(client, videos, token):
    response = client.get("/videos/", headers={'Authorization': token})
    assert response.status_code == 200
    assert b"Video teste 1" in response.data


def test_videos_GET_by_id(client, videos):
    response = client.get("/videos/2/")
    assert response.status_code == 200
    assert b"Video teste 2" in response.data


def test_videos_GET_by_id_with_invalid_id(client, videos):
    response = client.get("/videos/15/")
    assert response.status_code == 404
    assert b"video not found" in response.data


def test_videos_GET_filter_search_teste_1(client, videos):
    response = client.get("/videos/?search=teste 1")
    assert response.status_code == 200
    assert b"teste 1" in response.data


def test_videos_GET_filter_with_no_data_search_teste_4(client, videos):
    response = client.get("/videos/?search=teste 4")
    assert response.status_code == 200
    assert b"[]" in response.data


def test_videos_pagination_page_1(client, bulk_videos):
    response = client.get("/videos/?page=1")
    assert response.status_code == 200
    assert b"Video teste 0" in response.data
    assert b"Video teste 4" in response.data
    assert b"Video teste 5" not in response.data
    assert b"Video teste 6" not in response.data


def test_videos_pagination_page_99_not_exist(client, bulk_videos):
    response = client.get("/videos/?page=99")
    assert response.status_code == 400
    assert b"Wrong number of pages" in response.data


@mark.c
def test_videos_POST_with_valid_json(client, videos):
    data = {
        "title": "Video teste 3",
        "description": "Meu terceiro video",
        "url": "https://www.google.com/",
    }
    response = client.post("/videos/", json=data)
    assert response.status_code == 201
    assert b"Video teste 3" in response.data
    assert b"Meu terceiro video" in response.data
    assert b"https://www.google.com/" in response.data
    assert b'"category_id": 1' in response.data


def test_videos_POST_with_valid_json_and_category_id(client, videos):
    data = {
        "title": "Video teste 3",
        "description": "Meu terceiro video",
        "url": "https://www.google.com/",
        "category_id": 2,
    }
    response = client.post("/videos/", json=data)
    assert response.status_code == 201
    assert b"Video teste 3" in response.data
    assert b"Meu terceiro video" in response.data
    assert b'"category_id": 2' in response.data


def test_videos_POST_with_invalid_json_missing_field(client, videos):
    data = {"title": "Video teste 3", "url": "https://www.google.com/"}
    response = client.post("/videos/", json=data)
    assert response.status_code == 400
    assert b"Missing data for required field." in response.data


def test_videos_POST_with_invalid_json_more_fields(client, videos):
    data = {
        "title": "Video teste 3",
        "description": "Meu terceiro video",
        "url": "https://www.google.com/",
        "ola": 123,
    }
    response = client.post("/videos/", json=data)
    assert response.status_code == 400
    assert b"Unknown field." in response.data


def test_videos_POST_with_invalid_json_blank_fields(client, videos):
    data = {
        "title": "",
        "description": "Meu terceiro video",
        "url": "https://www.google.com/",
    }
    response = client.post("/videos/", json=data)
    assert response.status_code == 400
    assert b"Must not blank" in response.data


def test_videos_PUT_with_valid_json(client, videos):
    data = {
        "title": "Video teste 1 atualizado",
        "description": "Meu terceiro video atualizado",
        "url": "https://www.google.com/",
    }
    response = client.put("/videos/1/", json=data)
    assert response.status_code == 200
    assert b"Video teste 1 atualizado" in response.data
    assert b"Meu terceiro video atualizado" in response.data
    assert b"https://www.google.com/" in response.data


def test_videos_PUT_with_invalid_json_with_invalid_id(client, videos):
    data = {
        "title": "Video teste 1 atualizado",
        "description": "Meu terceiro video atualizado",
        "url": "https://www.google.com/",
    }
    response = client.put("/videos/15/", json=data)
    assert response.status_code == 404
    assert b"video not found" in response.data


def test_videos_PUT_with_invalid_json_missing_fields(client, videos):
    data = {
        "description": "Meu terceiro video atualizado",
        "url": "https://www.google.com/",
    }
    response = client.put("/videos/1/", json=data)
    assert response.status_code == 400
    assert b"Missing data for required field." in response.data


def test_videos_PUT_with_invalid_json_more_fields(client, videos):
    data = {
        "description": "Meu terceiro video atualizado",
        "url": "https://www.google.com/",
        "ola": 123,
    }
    response = client.put("/videos/1/", json=data)
    assert response.status_code == 400
    assert b"Unknown field" in response.data


def test_videos_PUT_with_invalid_json_blank_fields(client, videos):
    data = {"description": "", "url": "https://www.google.com/"}
    response = client.put("/videos/1/", json=data)
    assert response.status_code == 400
    assert b"Must not blank." in response.data


def test_videos_PATCH_with_valid_json(client, videos):
    data = {"title": "Video teste 1 atualizado"}
    response = client.patch("/videos/1/", json=data)
    assert response.status_code == 200
    assert b'"id": 1' in response.data
    assert b"Video teste 1 atualizado" in response.data


def test_videos_PATCH_with_invalid_json_blank_fields(client, videos):
    data = {"title": ""}
    response = client.patch("/videos/1/", json=data)
    assert response.status_code == 400
    assert b"Must not blank" in response.data


def test_videos_PATCH_with_invalid_json_blank_fields(client, videos):
    data = {"description": "", "url": "https://www.google.com/"}
    response = client.patch("/videos/1/", json=data)
    assert response.status_code == 400
    assert b"Must not blank." in response.data


def test_videos_DELETE(client, videos):
    response = client.delete("/videos/1/")
    assert response.status_code == 200
    assert b"successfully deleted" in response.data


def test_videos_DELETE_wrong_id(client, videos):
    response = client.delete("/videos/4/")
    assert response.status_code == 404
    assert b"fail to delete, video not found" in response.data
