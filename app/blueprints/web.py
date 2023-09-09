from flask import Blueprint, request

bp = Blueprint('web', __name__)


@bp.route("/")
def home():
    return "<p>Hello, web route!</p>"
