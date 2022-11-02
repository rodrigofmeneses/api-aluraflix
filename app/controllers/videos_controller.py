from flask import Blueprint, jsonify, request, json
from marshmallow import ValidationError

from app.controllers.utils import validate_json
from app.models import Videos
from app.ext.database import db
from app.ext.schemas.videos_schema import video_schema


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def get_all_videos():
    '''Get all videos.'''
    videos = Videos.query.all()
    return video_schema.dump(videos, many=True), 200

@videos.get('/<int:id>')
def get_video_by_id(id):
    '''Get video by id.'''
    video = Videos.query.get(id)
    if not video:
        return jsonify({'message': 'video not found'}), 404
    return video_schema.dump(video), 200

@videos.post('/')
def add_video():
    '''Add video with POST method. Request JSON body must be validade.
    Validation consists in all fields present without nullable values.
    '''
    json_data = request.get_json()
    try:
        data = video_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    # breakpoint()
    video = Videos(**data)
    db.session.add(video)
    db.session.commit()
    return video_schema.dump(video), 201
    

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
    return video_schema.dump(video), 200
    
@videos.delete('/<int:id>')
def delete_video_by_id(id):
    video = Videos.query.get(id)
    if not video:
        return jsonify({'message': 'fail to delete, video not found'}), 404
    try:
        db.session.delete(video)
        db.session.commit()
    except:
        return jsonify({'message': 'something wrong'}), 400
    return jsonify({'message': 'successfully deleted'}), 200