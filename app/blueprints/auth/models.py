from app.extensions import db
from app.blueprints.image.models import InstagramUser
#pylint: disable=no-init, too-few-public-methods

class User(db.Document):
    """A user of the gramHammer web application."""
    username = db.StringField(required=True, unique=True)
    instagram_username = db.ReferenceField(InstagramUser)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
