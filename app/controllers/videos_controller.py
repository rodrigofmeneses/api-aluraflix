from flask import Blueprint, jsonify, request, json
from app.models import Videos
from app.ext.database import db


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def get_all_videos():
    videos = Videos.query.all()
    return jsonify([video.serializer() for video in videos]), 200

@videos.get('/<int:id>')
def get_video_by_id(id):
    video = Videos.query.get(id)
    if not video:
        return jsonify({'message': 'video not found'}), 404
    return jsonify(video.serializer()), 200

@videos.post('/')
def add_video():
    data = request.get_json()
    try:
        id = data['id']
        titulo = data['titulo']
        descricao = data['descricao']
        url = data['url']
        video = Videos(id=id, titulo=titulo, descricao=descricao, url=url)
        db.session.add(video)
        db.session.commit()
    except:
        return jsonify({'message': 'something wrong'}), 400
    return jsonify(data), 201
    

@videos.put('/<int:id>')
def update_video_by_id(id):
    data = request.get_json()
    video = Videos.query.get(id)
    if not video:
        return jsonify({'message': 'video not found'}), 404
    if video.id == data['id']:
        return jsonify({'message': 'id not valid'}), 406
    try:
        video.id = data['id']
        video.titulo = data['titulo']
        video.descricao = data['descricao']
        video.url = data['url']
        db.session.add(video)
        db.session.commit()
    except:
        return jsonify({'message': 'something wrong'}), 406
    return jsonify(data), 200
    