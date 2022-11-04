from app.controllers.videos_controller import videos
from app.controllers.categorias_controller import categorias


def init_app(app):
    app.register_blueprint(videos)
    app.register_blueprint(categorias)