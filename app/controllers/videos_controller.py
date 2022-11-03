from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.models import Video
from app.ext.database import db
from app.ext.schemas.videos_schema import video_schema


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def get_all_videos():
    '''Get all videos.'''
    videos = Video.query.all()
    return video_schema.dump(videos, many=True), 200

@videos.get('/<int:id>')
def get_video_by_id(id):
    '''Get video by id.'''
    video = Video.query.get(id)
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
        video = video_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
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
        
    json_data = request.get_json()
    video = Video.query.get(id)
    
    if not video:
        return jsonify({'message': 'video not found'}), 404
    match request.method:
        case 'PUT':
            try:
                # breakpoint()
                video_schema.load(json_data)
            except ValidationError as err:
                return err.messages, 400
        case 'PATCH':
            try:
                video_schema.load(json_data, partial=True)
            except ValidationError as err:
                return err.messages, 400
    
    video.query.update(json_data)
    db.session.commit()
    return video_schema.dump(video), 200

    
@videos.delete('/<int:id>')
def delete_video_by_id(id):
    video = Video.query.get(id)
    if not video:
        return jsonify({'message': 'fail to delete, video not found'}), 404
    db.session.delete(video)
    db.session.commit()
    return jsonify({'message': 'successfully deleted'}), 200