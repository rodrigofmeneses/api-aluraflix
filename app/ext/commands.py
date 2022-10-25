from app.ext.database import db
from app.models import Videos

def create_db():
    '''Create database'''
    db.create_all()

def drop_db():
    '''Drop database'''
    db.drop_all()

def populate_db():
    '''Populate database'''
    videos = [
        Videos(
            titulo='Video teste 1',
            descricao='Meu primeiro video',
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        ),
        Videos(
            titulo='Video teste 2',
            descricao='Meu segundo video',
            url='https://www.youtube.com/watch?v=xFrGuyw1V8s'
        ),
    ]
    db.session.bulk_save_objects(videos)
    db.session.commit()

def init_app(app):
    '''Registry commands on flask'''
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
        