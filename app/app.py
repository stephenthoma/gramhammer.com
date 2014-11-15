import os

from flask import Flask
from extensions import db
from blueprints.home.views import home
from blueprints.auth.views import auth

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
app.register_blueprint(auth, url_prefix='/api/auth')
