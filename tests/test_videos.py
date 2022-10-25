from app import create_app


def test_videos_get():
    app = create_app()
    
    with app.test_client() as client:
        response = client.get('/videos/')
        assert response.status_code == 200
        assert b'"titulo": "Video teste 1"' in response.data