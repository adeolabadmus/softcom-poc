import os

from flask import Flask

from ..settings import config_type
from helpers import initialize_extensions, register_blueprints


def create_app(package_name):
    app = Flask(package_name)

    config = config_type[os.environ.get('FLASK_CONFIG')]
    app.config.from_object(config)

    initialize_extensions(app)
    register_blueprints(app, package_name)
    # register error handlers
    return app
