from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/')
def api():
    return jsonify(success="True")
