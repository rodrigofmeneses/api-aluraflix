from pytest import mark


def test_categories_GET(client, categories):
    response = client.get("/categories/")
    assert response.status_code == 200
    assert b"LIVRE" in response.data
    assert b"category teste 1" in response.data


def test_categories_GET_by_id(client, categories):
    response = client.get("/categories/2/")
    assert response.status_code == 200
    assert b"category teste 1" in response.data


def test_categories_GET_by_id_with_invalid_id(client, categories):
    response = client.get("/categories/15/")
    assert response.status_code == 404
    assert b"category not found" in response.data


def test_categories_POST_with_valid_json(client, categories):
    data = {"title": "Terror", "color": "black"}
    response = client.post("/categories/", json=data)
    assert response.status_code == 201
    assert b"Terror" in response.data
    assert b"black" in response.data


def test_categories_POST_with_invalid_json_missing_field(client, categories):
    data = {
        "title": "Terror",
    }
    response = client.post("/categories/", json=data)
    assert response.status_code == 400
    assert b"Missing data for required field." in response.data


def test_categories_POST_with_invalid_json_more_fields(client, categories):
    data = {"title": "Video teste 3", "color": "black", "ola": 123}
    response = client.post("/categories/", json=data)
    assert response.status_code == 400
    assert b"Unknown field." in response.data


def test_categories_POST_with_invalid_json_blank_fields(client, categories):
    data = {"title": "", "color": ""}
    response = client.post("/categories/", json=data)
    assert response.status_code == 400
    assert b"Must not blank" in response.data


def test_categories_PUT_with_valid_json(client, categories):
    data = {"title": "title atualizado", "color": "color atualizada"}
    response = client.put("/categories/1/", json=data)
    assert response.status_code == 200
    assert b"title atualizado" in response.data
    assert b"color atualizada" in response.data


def test_categories_PUT_with_invalid_json_invalid_id(client, categories):
    data = {"title": "Terror", "color": "black"}
    response = client.put("/categories/15/", json=data)
    assert response.status_code == 404
    assert b"category not found" in response.data


def test_categories_PUT_with_invalid_json_missing_fields(client, categories):
    data = {
        "title": "Terror",
    }
    response = client.put("/categories/1/", json=data)
    assert response.status_code == 400
    assert b"Missing data for required field." in response.data


def test_categories_PUT_with_invalid_json_more_fields(client, categories):
    data = {"title": "Terror", "color": "black", "ola": 123}
    response = client.put("/categories/1/", json=data)
    assert response.status_code == 400
    assert b"Unknown field" in response.data


def test_categories_PUT_with_invalid_json_blank_fields(client, categories):
    data = {"title": "", "color": "black"}
    response = client.put("/categories/1/", json=data)
    assert response.status_code == 400
    assert b"Must not blank." in response.data


def test_categories_PATCH_with_valid_json(client, categories):
    data = {"color": "green"}
    response = client.patch("/categories/1/", json=data)
    assert response.status_code == 200
    assert b'"id": 1' in response.data
    assert b"green" in response.data


def test_categories_PATCH_with_invalid_json_blank_fields(client, categories):
    data = {
        "color": "",
    }
    response = client.patch("/categories/1/", json=data)
    assert response.status_code == 400
    assert b"Must not blank" in response.data


def test_categories_DELETE(client, categories):
    response = client.delete("/categories/1/")
    assert response.status_code == 200
    assert b"successfully deleted" in response.data


def test_categories_DELETE_wrong_id(client, categories):
    response = client.delete("/categories/4/")
    assert response.status_code == 404
    assert b"fail to delete, category not found" in response.data


def test_categories_GET_all_videos_by_category_id(client, categories, videos):
    response = client.get("/categories/2/videos/")
    assert response.status_code == 200
    assert b"Video teste 2" in response.data
    assert b"Meu segundo video" in response.data
    assert b"Video teste 3" in response.data
    assert b"Meu terceiro video" in response.data
