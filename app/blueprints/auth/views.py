from flask import Blueprint, jsonify, request, session, redirect
from app.extensions import instagram_API as InstagramAPI

auth = Blueprint('auth', __name__)


@auth.route('/authenticate')
def authenticate():
    return jsonify({'success': 'True'})


@auth.route('/register')
def register():
    return jsonify({'success': 'True'})

@auth.route('/instagram_connect')
def instagram_connect():
    """Redirect user to Instagram authorization page."""
    url = InstagramAPI.get_authorize_url(scope=['likes', 'comments', 'relationships'])
    return redirect(url)

@auth.route('/instagram_callback')
def instagram_callback():
    """Instagram will redirect users to this endpoint after successful auth."""
    code = request.args.get('code')
    if code:
        access_token, user = InstagramAPI.exchange_code_for_access_token(code)
        if not access_token:
            return 'Could not get access token'

        session['instagram_access_token'] = access_token
        session['instagram_user'] = user

        return redirect('/') # redirect back to main page
    else:
        return "No code provided."
