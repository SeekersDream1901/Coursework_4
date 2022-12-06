from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.auth import auth_ns
from app.views.director import directors_ns
from app.views.favorites_movie import favorites_movies_ns
from app.views.genre import genres_ns
from app.views.movie import movies_ns
from app.views.user import users_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(users_ns)
    api.add_namespace(favorites_movies_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)

    app.run()
