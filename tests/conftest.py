from app import create_app
from app.ext.database import db
from pytest import fixture

from app.models import Video


@fixture(scope='module')
def client():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        db.create_all()
        yield client
        db.drop_all()
        db.session.remove()

@fixture
def videos(client):
    videos = [
        Video(
            titulo='Video teste 1',
            descricao='Meu primeiro video',
            url='https://www.google.com/'
        ),
        Video(
            titulo='Video teste 2',
            descricao='Meu segundo video',
            url='https://www.google.com/'
        ),
    ]
    db.session.bulk_save_objects(videos)
    db.session.commit()
    
    yield videos

    try:
        for video in Video.query.all():
            db.session.delete(video)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()