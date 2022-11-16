from flask import Blueprint, request
from marshmallow import ValidationError

from app.ext.database import db
from app.ext.schemas.categories_schema import category_schema
from app.ext.schemas.videos_schema import video_schema
from app.models import Category


categories = Blueprint("categories", __name__, url_prefix="/categories")


@categories.get("/")
def get_categories():
    """Get all categories.
    Return:
        Response JSON with all categories and status code.
    """
    categories = Category.query.all()
    return {"categories": category_schema.dump(categories, many=True)}, 200


@categories.get("/<int:id>/")
def get_category_by_id(id: int):
    """Get category by id.
    Args:
        id (int): category id.
    Return:
        Response JSON with category or error message and status code.
    """
    category = Category.query.get(id)
    if not category:
        return {"message": "category not found"}, 404
    return category_schema.dump(category), 200


@categories.get("/<int:id>/videos/")
def get_all_videos_by_category(id: int):
    """Get all videos by category.
    Args:
        id (int): category id.
    Return:
        Response JSON with all videos of category id
    """
    category = Category.query.get(id)
    if not category:
        return {"message": "category not found"}, 404
    return {"videos": video_schema.dump(category.videos, many=True)}, 200


@categories.post("/")
def create_category():
    """Create category with POST method.
    Return:
        Response JSON with added category or error message and status code.
    """
    json_data = request.get_json()
    try:
        category = category_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    db.session.add(category)
    db.session.commit()
    return category_schema.dump(category), 201


@categories.route("/<int:id>/", methods=["PUT", "PATCH"])
def update_category_by_id(id: int):
    """Update category by id with POST
    Args:
        id (int): category id.
    Return:
        Response JSON with updated category or error message and status code.
    """
    json_data = request.get_json()
    category = Category.query.get(id)

    if not category:
        return {"message": "category not found"}, 404
    try:
        match request.method:
            case "PUT":
                category_schema.load(json_data)
            case "PATCH":
                category_schema.load(json_data, partial=True)
    except ValidationError as err:
        return err.messages, 400

    Category.query.filter_by(id=id).update(json_data)
    db.session.commit()
    return category_schema.dump(category), 200


@categories.delete("/<int:id>/")
def delete_category_by_id(id: int):
    category = Category.query.get(id)
    if not category:
        return {"message": "fail to delete, category not found"}, 404
    db.session.delete(category)
    db.session.commit()
    return {"message": "successfully deleted"}, 200
