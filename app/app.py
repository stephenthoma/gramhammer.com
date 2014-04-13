import os

from flask import Flask
from extensions import db
from blueprints.about import about
from blueprints.accounts import accounts
from blueprints.api import api

## App ##
app = Flask(__name__, static_folder='static',
            template_folder='templates')

## Config ##
flask_env = os.environ.get('FLASK_ENV')
if flask_env is None:
    app.config.from_pyfile('config/dev.py')
else:
    app.config.from_pyfile('config/' + flask_env + '.py')

## Database ##
db.init_app(app)
db.app = app

## Blueprints ##
app.register_blueprint(about, url_prefix='/about')
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(api, url_prefix='/api')
