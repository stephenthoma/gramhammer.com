from flask.ext.cache import Cache
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.assets import Environment, Bundle

## Init ##
cache = Cache()
mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
assets = Environment()

## Assets ##
js_libs = Bundle('js/libs/jquery.js', 'js/libs/underscore.js',
                 'js/libs/backbone.js', 'js/libs/bootstrap.js',
                 'js/libs/bootstrap.js', filters='jsmin',
                 output='gen/libs.js')
js_main = Bundle('js/app.js', 'js/main.js', filters='jsmin',
                 output='gen/main.js')
less = Bundle('less/main.less', filters='less', output='gen/main.css')
