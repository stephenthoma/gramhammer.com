import os


class Config(object):
    ''' Default Config Object '''
    DEBUG = False
    TESTING = False
    PORT = int(os.environ.get('PORT', 5000))


class ProductionConfig(Config):
    '''Production Config Object'''
    pass


class DevelopmentConfig(Config):
    '''Development Config Object'''
    DEBUG = True
