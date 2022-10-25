from app.controllers.videos import videos


def init_app(app):
    app.register_blueprint(videos)