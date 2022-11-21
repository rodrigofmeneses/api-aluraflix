from app.ext.database import db
from app.models import Video, Category
from faker import Faker

from random import randint


def create_db():
    """Create database"""
    db.create_all()
    category = Category(title="FREE", color="ffffff")
    db.session.add(category)
    db.session.commit()


def drop_db():
    """Drop database"""
    db.drop_all()


def populate_db():
    """Populate database"""
    faker = Faker()
    categories = [Category(title=f"Test Category {i}", color=faker.color()) for i in range(5)]
    videos = [
        Video(
            title=f"Test Video {i}",
            description=faker.text(),
            url=faker.url(),
            category_id=randint(1, 5),
        )
        for i in range(10)
    ]
    db.session.bulk_save_objects(categories)
    db.session.bulk_save_objects(videos)
    db.session.commit()


def init_app(app):
    """Registry commands on flask"""
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
