from flask import Blueprint, jsonify
from app.models import Videos


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def index():
    videos = Videos.query.all()
    return jsonify([video.serializer() for video in videos]), 200

@videos.get('/<int:id>')
def video_id(id):
    video = Videos.query.filter_by(id=id).first()
    if not video:
        return jsonify({"message": "video not found"}), 404
    return jsonify(video.serializer()), 200