import os
from flask import Flask
from flask.ext.mail import Mail

from config import config
from extensions import db

from blueprints.home.views import home
from blueprints.auth.views import auth

def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(auth, url_prefix='/api/auth')

def create_app(config_name):
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
