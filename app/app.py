from flask import Flask
from extensions import db
from .main import main
from .user import user
from .api import api

# App
app = Flask(__name__, static_folder='static',
            template_folder='templates')
app.config.from_pyfile('config.py')

# Extensions
db.init_app(app)
db.app = app
db.create_all()

# Blueprints
app.register_blueprint(main)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(api, url_prefix='/api')
