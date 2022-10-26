from flask import session
from app import create_app
from app.ext.database import db
from pytest import fixture

from app.models import Videos


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
        Videos(
            id=1,
            titulo='Video teste 1',
            descricao='Meu primeiro video',
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        ),
        Videos(
            id=2,
            titulo='Video teste 2',
            descricao='Meu segundo video',
            url='https://www.youtube.com/watch?v=xFrGuyw1V8s'
        ),
    ]
    db.session.bulk_save_objects(videos)
    db.session.commit()
    
    yield videos

    try:
        for video in Videos.query.all():
            db.session.delete(video)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()