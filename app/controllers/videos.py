from flask import Blueprint, jsonify, request, json
from app.models import Videos
from app.ext.database import db


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def index():
    videos = Videos.query.all()
    return jsonify([video.serializer() for video in videos]), 200

@videos.get('/<int:id>')
def video_id(id):
    video = Videos.query.filter_by(id=id).first()
    if not video:
        return jsonify({'message': 'video not found'}), 404
    return jsonify(video.serializer()), 200

@videos.post('/')
def add_video():
    request_data = request.get_json()
    try:
        titulo = request_data['titulo']
        descricao = request_data['descricao']
        url = request_data['url']
        video = Videos(titulo=titulo, descricao=descricao, url=url)
        db.session.add(video)
        db.session.commit()
    except:
        return jsonify({'message': 'something wrong'}), 400
    return jsonify(request_data), 201
    