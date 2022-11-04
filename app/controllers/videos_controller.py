from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequestKeyError

from app.models import Video
from app.ext.database import db
from app.ext.schemas.videos_schema import video_schema


videos = Blueprint('videos', __name__, url_prefix='/videos')

@videos.get('/')
def get_all_videos():
    '''Get all videos.
        Return:
            Response JSON with all videos and status code.
    '''
    if not request.args:
        all_videos = Video.query.all()
        return {'videos': video_schema.dump(all_videos, many=True)}, 200
    
    try:
        target = request.args['search']
    except BadRequestKeyError:
        return {'message': 'to filter a video use ?search=video_title'}, 400
    
    filter_videos = Video.query.filter(Video.titulo.like(f'%{target}%')).all()
    return {'videos': video_schema.dump(filter_videos, many=True)}, 200 
    

@videos.get('/<int:id>')
def get_video_by_id(id):
    '''Get video by id.
        Args:
            id (int): Video id.
        Return:
            Response JSON with video or error message and status code.
    '''
    video = Video.query.get(id)
    if not video:
        return jsonify({'message': 'video not found'}), 404
    return video_schema.dump(video), 200

@videos.post('/')
def add_video():
    '''Add video with POST method.
        Return:
            Response JSON with added video or error message and status code.
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
    '''Update video by id with PUT and PATCH methods.
        Args:
            id (int): Video id.
        Return:
            Response JSON with updated video or error message and status code.
    '''
    json_data = request.get_json()
    video = Video.query.get(id)
    
    if not video:
        return jsonify({'message': 'video not found'}), 404
    try:
        match request.method:
            case 'PUT':
                video_schema.load(json_data)
            case 'PATCH':
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