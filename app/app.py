from flask import Flask
from extensions import db
from .main import main

# App 
app = Flask(__name__, static_folder='static',
            template_folder='templates') 
app.config.from_pyfile('config.py') 
 
# Extensions
db.init_app(app)

# Blueprints 
app.register_blueprint(main)
