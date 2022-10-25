from flask import Blueprint, jsonify
from app.models import Videos


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def index():
    videos = Videos.query.all()
    return jsonify([video.serializer() for video in videos]), 200