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
js_libs = Bundle('dev/js/libs/jquery.js', 'dev/js/libs/underscore.js',
                 'dev/js/libs/backbone.js', 'dev/js/libs/bootstrap.js',
                 'dev/js/libs/bootstrap.js', filters='jsmin',
                 output='prod/libs.js')
js_main = Bundle('dev/js/app.js', 'dev/js/main.js', filters='jsmin',
                 output='prod/main.js')
less = Bundle('dev/less/main.less', filters='less', output='prod/main.css')
