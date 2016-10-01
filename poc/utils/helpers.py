import importlib

from flask import Blueprint


class BlueprintWrapper(object):
    def __init__(self, name, package_name, url_prefix):
        self.blueprint = Blueprint(name, package_name, url_prefix=url_prefix)
        self.name = name

    def __repr__(self):
        return '<Blueprint %s>' % self.name


def register_blueprints(app, package_name):
    package = importlib.import_module(package_name)
    for variable in dir(package):
        item = getattr(package, variable)
        if isinstance(item, BlueprintWrapper):
            controllers = '%s.%s.%s' % (package_name, item.name, 'controllers')
            errors = '%s.%s.%s' % (package_name, item.name, 'errors')
            importlib.import_module(controllers)
            importlib.import_module(errors)
            app.register_blueprint(item.blueprint)


def initialize_extensions(app):
    # create extension objects here
    # e.g. db = SQLAlchemy()
    # db.init(app)
    pass
