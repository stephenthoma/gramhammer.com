from app.extensions import db
#pylint: disable=no-init, too-few-public-methods, invalid-name

class InstagramUser(db.Document):
    """Metadata for Instagram user with tracked images."""
    id = db.StringField(required=True, primary_key=True)
    username = db.StringField(required=True)
    bio = db.StringField(required=True)
    profile_picture = db.StringField(required=True, unique=True)

class Image(db.Document):
    """Reference to an image on Instagram."""
    id = db.StringField(required=True, primary_key=True)
    user = db.ReferenceField(InstagramUser)
    url = db.StringField(required=True, unique=True)
    description = db.StringField(required=True)
    location = db.PointField()
