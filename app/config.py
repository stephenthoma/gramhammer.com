import os

class Config(object):
    ''' Default Config Object '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hunter2'
    DEBUG = False
    TESTING = False
    PORT = int(os.environ.get('PORT', 5000))
    SSL_DISABLE = False

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    INSTA_CONFIG = {
        'client_id': os.environ.get('CLIENT_ID'),
        'client_secret': os.environ.get('CLIENT_SECRET'),
        'redirect_uri': os.environ.get('REDIRECT_URI')
        }

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    '''Production Config Object'''
    pass


class DevelopmentConfig(Config):
    '''Development Config Object'''
    DEBUG = True
    MONGODB_SETTINGS = {'DB': "gramhammer"}


class TestingConfig(Config):
    '''Testing Config Object'''
    TESTING = True
    MONGODB_SETTINGS = {'DB': "gramhammer"}

config = {
    'default': DevelopmentConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
    }
