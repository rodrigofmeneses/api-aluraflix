from app.ext.database import db


def create_db():
    '''Create database'''
    db.create_all()

def drop_db():
    '''Drop database'''
    db.drop_all()

def populate_db():
    '''Populate database'''
    ...

def init_app(app):
    '''Registry commands on flask'''
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
    return app