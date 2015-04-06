from flask import Blueprint, jsonify
from app.blueprints.image.models import InstagramUser, Image

image = Blueprint('image', __name__)

@image.route('/')
def root():
    """Returns a randomly selected image"""
    # [TODO]: Check if image already shown
    # [TODO]: If no unshown images remain signal frontend discover CTA
    img = Image.objects[0] #pylint: disable=no-member
    return jsonify({
        'id': img.id,
        'url': img.url,
        'description': img.description,
        'user': img.user.username,
        'avatar': img.user.profile_picture
        })

"""Mark that the user has liked the image."""
@image.route('/<image_id>/like', methods=['POST'])
def like(image_id):
    return jsonify({'success': 'True'})

