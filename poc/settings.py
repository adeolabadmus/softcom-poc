import os


class Config(object):
    SECRET_KEY = os.environ.get('FLASK_POC_SECRET_KEY')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024


class Development(Config):
    DEBUG = True


class Production(Config):
    pass


class Test(Config):
    TESTING = True

config_type = {
    'development': Development,
    'production': Production,
    'testing': Test
}
