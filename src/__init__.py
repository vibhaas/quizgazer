from flask import Flask

from config import Config, DevelopmentConfig
from src.db import db


def create_app(config_class: type[Config] = DevelopmentConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from src.models import user  # noqa: F401
    from src.routes.main import main_bp

    app.register_blueprint(main_bp)
    return app
