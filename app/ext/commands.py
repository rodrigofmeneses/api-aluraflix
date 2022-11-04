from app.ext.database import db
from app.models import Video, Categoria


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
            titulo='Categoria test 1',
            cor='black'
        ),
        Categoria(
            titulo='Categoria test 2',
            cor='brown'
        ),
    ]
    videos = [
        Video(
            titulo='Video teste 1',
            descricao='Meu primeiro video',
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        ),
        Video(
            titulo='Video teste 2',
            descricao='Meu segundo video',
            url='https://www.youtube.com/watch?v=xFrGuyw1V8s'
        ),
    ]
    db.session.bulk_save_objects(categorias)
    db.session.bulk_save_objects(videos)
    db.session.commit()

def init_app(app):
    '''Registry commands on flask'''
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
