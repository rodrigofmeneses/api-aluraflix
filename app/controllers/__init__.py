from app.controllers.videos_controller import videos


def init_app(app):
    app.register_blueprint(videos)