from app.controllers.videos_controller import videos
from app.controllers.categories_controller import categories
from app.controllers.auth_controller import auth


def init_app(app):
    app.register_blueprint(videos)
    app.register_blueprint(categories)
    app.register_blueprint(auth)
