from flask import Blueprint, request
from marshmallow import ValidationError

from app.ext.database import db
from app.ext.schemas.categorias_schema import categoria_schema
from app.ext.schemas.videos_schema import video_schema
from app.models import Categoria


categorias = Blueprint('categorias', __name__, url_prefix='/categorias')

@categorias.get('/')
def get_categories():
    '''Get all categories.
        Return:
            Response JSON with all categorias and status code.
    '''
    categorias = Categoria.query.all()
    return {'categorias': categoria_schema.dump(categorias, many=True)}, 200

@categorias.get('/<int:id>')
def get_category_by_id(id: int):
    '''Get category by id.
        Args:
            id (int): Categoria id.
        Return:
            Response JSON with categoria or error message and status code.
    '''
    categoria = Categoria.query.get(id)
    if not categoria:
        return {'message': 'categoria not found'}, 404
    return categoria_schema.dump(categoria), 200

@categorias.get('/<int:id>/videos')
def get_all_videos_by_category(id: int):
    '''Get all videos by category.
        Args:
            id (int): Categoria id.
        Return:
            Response JSON with all videos of category id
    '''
    categoria = Categoria.query.get(id)
    if not categoria:
        return {'message': 'categoria not found'}, 404
    return {'videos': video_schema.dump(categoria.videos, many=True)}, 200

@categorias.post('/')
def create_categoria():
    '''Create categoria with POST method.
        Return:
            Response JSON with added categoria or error message and status code.
    '''
    json_data = request.get_json()
    try:
        categoria = categoria_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    db.session.add(categoria)
    db.session.commit()
    return categoria_schema.dump(categoria), 201

@categorias.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_categoria_by_id(id: int):
    '''Update categoria by id with POST
        Args:
            id (int): Categoria id.
        Return:
            Response JSON with updated categoria or error message and status code.
    '''
    json_data = request.get_json()
    categoria = Categoria.query.get(id)
    
    if not categoria:
        return {'message': 'categoria not found'}, 404
    try:
        match request.method:
            case 'PUT':
                    categoria_schema.load(json_data)
            case 'PATCH':
                    categoria_schema.load(json_data, partial=True)
    except ValidationError as err:
        return err.messages, 400
    
    Categoria.query.filter_by(id=id).update(json_data)
    db.session.commit()
    return categoria_schema.dump(categoria), 200

@categorias.delete('/<int:id>')
def delete_categoria_by_id(id: int):
    categoria = Categoria.query.get(id)
    if not categoria:
        return {'message': 'fail to delete, categoria not found'}, 404
    db.session.delete(categoria)
    db.session.commit()
    return {'message': 'successfully deleted'}, 200