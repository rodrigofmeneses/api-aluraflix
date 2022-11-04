from app import create_app
from app.ext.database import db
from pytest import fixture

from app.models import Video, Categoria


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
def categorias(client):
    categorias = [
        Categoria(
            titulo='LIVRE',
            cor='white'
        ),
        Categoria(
            titulo='Categoria teste 1',
            cor='Cor teste 1'
        ),
        Categoria(
            titulo='Categoria teste 2',
            cor='Cor teste 2'
        )
    ]
    db.session.bulk_save_objects(categorias)
    db.session.commit()

    yield videos

    try:
        for categoria in Categoria.query.all():
            db.session.delete(categoria)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()


@fixture
def videos(client, categorias):
    videos = [
        Video(
            titulo='Video teste 1',
            descricao='Meu primeiro video',
            url='https://www.google.com/'
        ),
        Video(
            titulo='Video teste 2',
            descricao='Meu segundo video',
            url='https://www.google.com/',
            categoria_id=2
        ),
        Video(
            titulo='Video teste 3',
            descricao='Meu terceiro video',
            url='https://www.google.com/',
            categoria_id=2
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