import os

from flask import Flask
from app.extensions import db
from app.blueprints.home.views import home

## App ##
app = Flask(__name__, static_folder='static',
            template_folder='templates')

## Config ##
flask_env = os.environ.get('FLASK_ENV')

if flask_env is None:
    app.config.from_object('app.config.DevelopmentConfig')
else:
    app.config.from_pyfile('app.config.%sConfig') % flask_env

## Database ##
db.init_app(app)
db.app = app

## Blueprints ##
app.register_blueprint(home)
