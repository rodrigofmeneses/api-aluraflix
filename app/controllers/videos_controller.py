from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

from app.models import Video
from app.ext.database import db
from app.ext.schemas.videos_schema import video_schema

ROWS_PER_PAGE = 5


videos = Blueprint("videos", __name__, url_prefix="/videos")


@videos.get("/")
def get_videos():
    """Get all videos.
    Return:
        Response JSON with all videos and status code.
    """
    page = request.args.get("page", default=1, type=int)
    search = request.args.get("search")

    query = Video.query
    if search:
        query = Video.query.filter(Video.title.like(f"%{search}%"))

    try:
        videos = query.paginate(page=page, per_page=ROWS_PER_PAGE)
    except NotFound:
        return {"message": "Wrong number of pages"}, 400

    response = {
        "count": videos.total,
        "next": None
        if not videos.has_next
        else f"{request.base_url}?page={videos.next_num}",
        "previous": None
        if not videos.has_prev
        else f"{request.base_url}?page={videos.prev_num}",
        "results": video_schema.dump(videos.items, many=True),
    }

    return response, 200


@videos.get("/<int:id>/")
def get_video_by_id(id):
    """Get video by id.
    Args:
        id (int): Video id.
    Return:
        Response JSON with video or error message and status code.
    """
    video = Video.query.get(id)

    if not video:
        return {"message": "video not found"}, 404

    return video_schema.dump(video), 200


@videos.post("/")
def create_video():
    """Create video with POST method.
    Return:
        Response JSON with added video or error message and status code.
    """
    json_data = request.get_json()

    try:
        video = video_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(video)
    db.session.commit()

    return video_schema.dump(video), 201


@videos.route("/<int:id>/", methods=["PUT", "PATCH"])
def update_video_by_id(id):
    """Update video by id with PUT and PATCH methods.
    Args:
        id (int): Video id.
    Return:
        Response JSON with updated video or error message and status code.
    """
    json_data = request.get_json()
    video = Video.query.get(id)

    if not video:
        return {"message": "video not found"}, 404
    try:
        match request.method:
            case "PUT":
                video_schema.load(json_data)
            case "PATCH":
                video_schema.load(json_data, partial=True)
    except ValidationError as err:
        return err.messages, 400

    Video.query.filter_by(id=id).update(json_data)
    db.session.commit()

    return video_schema.dump(video), 200


@videos.delete("/<int:id>/")
def delete_video_by_id(id):
    """Delete video by id with DELETE methods.
    Args:
        id (int): Video id.
    Return:
        Response message with successfull or fail delete.
    """
    video = Video.query.get(id)

    if not video:
        return {"message": "fail to delete, video not found"}, 404

    db.session.delete(video)
    db.session.commit()

    return {"message": "successfully deleted"}, 200
