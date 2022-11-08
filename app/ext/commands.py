from app.ext.database import db
from app.models import Video, Categoria

from random import randint


def create_db():
    '''Create database'''
    db.create_all()
    categoria = Categoria(
        titulo='LIVRE',
        cor='white'
    )
    db.session.add(categoria)
    db.session.commit()

def drop_db():
    '''Drop database'''
    db.drop_all()

def populate_db():
    '''Populate database'''
    categorias = [
        Categoria(
            titulo=f'Categoria test {i}',
            cor='black'
        ) for i in range(5)
    ]
    videos = [
        Video(
            titulo=f'Video teste {i}',
            descricao='Meu primeiro video',
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            categoria_id=randint(1, 5)
        ) for i in range(10)
    ]
    db.session.bulk_save_objects(categorias)
    db.session.bulk_save_objects(videos)
    db.session.commit()

def init_app(app):
    '''Registry commands on flask'''
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
