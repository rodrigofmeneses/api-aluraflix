from app.controllers.videos_controller import videos
from app.controllers.categories_controller import categories


def init_app(app):
    app.register_blueprint(videos)
    app.register_blueprint(categories)