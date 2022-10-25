from app import create_app


def test_videos_get():
    app = create_app()
    
    with app.test_client() as client:
        response = client.get('/videos/')
        assert response.status_code == 200
        assert b'"titulo": "Video teste 1"' in response.data

def test_videos_get_by_id():
    app = create_app()
    
    with app.test_client() as client:
        response = client.get('/videos/2')
        assert response.status_code == 200
        assert b'"titulo": "Video teste 2"' in response.data