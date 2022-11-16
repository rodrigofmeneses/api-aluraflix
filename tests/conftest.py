from app import create_app
from app.ext.database import db
from pytest import fixture
from random import randint

from app.models import User, Video, Category


@fixture(scope="module")
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
def categories(client):
    categories = [
        Category(title="LIVRE", color="white"),
        Category(title="category teste 1", color="color teste 1"),
        Category(title="category teste 2", color="color teste 2"),
    ]
    db.session.bulk_save_objects(categories)
    db.session.commit()

    yield videos

    try:
        for category in Category.query.all():
            db.session.delete(category)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()


@fixture
def bulk_videos(client, categories):
    videos = [
        Video(
            title=f"Video teste {i}",
            description="Meu primeiro video",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            category_id=randint(1, 3),
        )
        for i in range(20)
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


@fixture
def videos(client, categories):
    videos = [
        Video(
            title="Video teste 1",
            description="Meu primeiro video",
            url="https://www.google.com/",
        ),
        Video(
            title="Video teste 2",
            description="Meu segundo video",
            url="https://www.google.com/",
            category_id=2,
        ),
        Video(
            title="Video teste 3",
            description="Meu terceiro video",
            url="https://www.google.com/",
            category_id=2,
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


@fixture
def users(client):
    users = [
        User(username='rodrigo', password='1234'),
        User(username='marta', password='4321')
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()

    yield users

    try:
        for user in User.query.all():
            db.session.delete(user)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()