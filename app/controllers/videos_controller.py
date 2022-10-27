from flask import Blueprint, jsonify, request, json
from app.controllers.utils import validate_json
from app.models import Videos
from app.ext.database import db


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def get_all_videos():
    '''Get all videos.'''
    videos = Videos.query.all()
    return jsonify([video.serializer() for video in videos]), 200

@videos.get('/<int:id>')
def get_video_by_id(id):
    '''Get video by id.'''
    video = Videos.query.get(id)
    if not video:
        return jsonify({'message': 'video not found'}), 404
    return jsonify(video.serializer()), 200

@videos.post('/')
def add_video():
    '''Add video with POST method. Request JSON body must be validade.
    Validation consists in all fields present without nullable values.
    '''
    data = request.get_json()
    if not validate_json(data):
        return jsonify({'message': 'json body not allowed, key error'}), 400
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
    return jsonify(video.serializer()), 201
    

@videos.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_video_by_id(id):
    '''Update video by id with POST method. Request JSON body must be validade.
    Validation consists in all fields present without nullable values.
    
        Args:
            id (int): Video id.

        Return:
            Response JSON with updated video or error message and status code.
    '''
    data = request.get_json()
    video = Videos.query.get(id)
    if not video:
        return jsonify({'message': 'video not found'}), 404
    match request.method:
        case 'PUT':
            if not validate_json(data, method='PUT'):
                return jsonify({'message': 'json body not allowed'}), 400
            # for key in data.keys():
            #     setattr(video, key, data[key])
            # video.id = data['id']
            # video.titulo = data['titulo']
            # video.descricao = data['descricao']
            # video.url = data['url']
        case 'PATCH':
            if not validate_json(data, method='PATCH'):
                return jsonify({'message': 'json body not allowed'}), 400

    try:
        for key in data.keys():
            setattr(video, key, data[key])
        db.session.add(video)
        db.session.commit()
    except:
        return jsonify({'message': 'something wrong'}), 400
    return jsonify(video.serializer()), 200
    
@videos.patch('/<int:id>')
def update_video_by_id_patch(id):
    data = request.get_json()
