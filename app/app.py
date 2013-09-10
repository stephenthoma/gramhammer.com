from flask import Flask
from extensions import db, assets
from extensions import js_libs, js_main, less
from blueprints import core
from blueprints import about
from blueprints import api

## App ##
app = Flask(__name__, static_folder='static',
            template_folder='templates')
app.config.from_pyfile('config.py')

## Database ##
db.init_app(app)
db.app = app
db.create_all()

## Assets ##
assets.init_app(app)
assets.register('js_libs', js_libs)
assets.register('js_main', js_main)
assets.register('css_main', less)

## Blueprints ##
app.register_blueprint(core)
app.register_blueprint(about, url_prefix='/about')
app.register_blueprint(api, url_prefix='/api')
