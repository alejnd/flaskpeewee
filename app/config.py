import os

class Config(object):
    DEBUG        = False
    TESTING      = False
    DATABASE     = ':memory:'
    CSRF_ENABLED = True
    SECRET_KEY   = os.urandom(24)
    HOST         = '172.0.0.1'

class ProductionConfig(Config):
    DATABASE = 'production.db'
    HOST     = '0.0.0.0'

class DevelopmentConfig(Config):
    DEBUG    = True
    DATABASE = 'develpment.db'

class TestingConfig(Config):
    TESTING = True

config = DevelopmentConfig()
