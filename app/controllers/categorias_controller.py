from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.models import Categoria
from app.ext.database import db
from app.ext.schemas.categorias_schema import categoria_schema


categorias = Blueprint('categorias', __name__, url_prefix='/categorias')

@categorias.get('/')
def get_all_categories():
    '''Get all categories.
        Return:
            Response JSON with all categorias and status code.
    '''
    categorias = Categoria.query.all()
    return categoria_schema.dump(categorias, many=True), 200

@categorias.get('/<int:id>')
def get_category_by_id(id):
    '''Get category by id.'''
    categoria = Categoria.query.get(id)
    if not categoria:
        return jsonify({'message': 'categoria not found'}), 404
    return categoria_schema.dump(categoria), 200

@categorias.post('/')
def add_categoria():
    '''Add categoria with POST method.'''
    json_data = request.get_json()
    try:
        categoria = categoria_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    db.session.add(categoria)
    db.session.commit()
    return categoria_schema.dump(categoria), 201