from flask.ext.mongoengine import MongoEngine
from instagram.client import InstagramAPI
import app

## Init ##
db = MongoEngine()

## Instagram ##
instagram_API = InstagramAPI(**app.config['default'].INSTA_CONFIG)
