from flask import Blueprint, jsonify

home = Blueprint('home', __name__)


@home.route('/')
def homepage():
    return jsonify({'success': "true"})
