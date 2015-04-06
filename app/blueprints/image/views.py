from flask import Blueprint, jsonify, session, redirect
from app.blueprints.image.models import Image
from app.extensions import instagram_API as InstagramAPI

image = Blueprint('image', __name__)

@image.route('/')
def root():
    """Returns a randomly selected image"""
    # [TODO]: Check if image already shown
    # [TODO]: If no unshown images remain signal frontend discover CTA
    # [TODO]: Un-hardcode the image
    img = Image.objects[0] #pylint: disable=no-member
    return jsonify({
        'id': img.id,
        'url': img.url,
        'description': img.description,
        'user': img.user.username,
        'avatar': img.user.profile_picture
        })

@image.route('/<image_id>/like', methods=['POST'])
def like(image_id):
    """Like image on Instagram, and mark image as liked.."""
    if 'instagram_access_token' in session and 'instagram_user' in session:
        userAPI = InstagramAPI
        userAPI.access_token = session['instagram_access_token']
        userAPI.client_ips = '127.0.0.1' # [TODO]: Get actual request IP
        try:
            userAPI.like_media(media_id=image_id)
        except:
            print 'Error liking media'
            return jsonify({'success': 'False'})
        else:
            # [TODO]: Mark that image is liked in DB.
            # str(image_id)?
            img = Image.objects(id=image_id).first() #pylint: disable=no-member
            return jsonify({'success': 'True'})
    else:
        return redirect('/api/auth/instagram_connect')

