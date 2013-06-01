from flask.ext.cache import Cache 
from flask.ext.mail import Mail 
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.bcrypt import Bcrypt

cache = Cache() 
mail = Mail() 
db = SQLAlchemy() 
bcrypt = Bcrypt() 
