import os
from flask import Flask
from flask.ext.mail import Mail

from app.config import config
from app.extensions import db

from app.blueprints.home.views import home
from app.blueprints.auth.views import auth
from app.blueprints.image.views import image

def register_blueprints(app):
    """Register the diverse sets of blueprints with the flask app."""
    app.register_blueprint(home)
    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(image, url_prefix='/api/image')

def create_app(config_name):
    """Initialize the flask app with external configuration."""
    ## App ##
    app = Flask(__name__, static_folder='static',
                template_folder='templates')

    ## Config ##
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    ## Database ##
    db.init_app(app)
    db.app = app

    ## Mail ##
    mail = Mail()
    mail.init_app(app)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)

    ## Blueprints ##
    register_blueprints(app)

    return app
