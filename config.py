import os

class Config(object):
    DEBUG        = False
    TESTING      = False
    DATABASE     = ':memory:'
    CSRF_ENABLED = True
    SECRET_KEY   = os.urandom(24)

class ProductionConfig(Config):
    DATABASE = 'production.db'

class DevelopmentConfig(Config):
    DEBUG    = True
    DATABASE = 'develpment.db'

class TestingConfig(Config):
    TESTING = True

config = DevelopmentConfig()
