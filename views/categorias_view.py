from flask import Blueprint, jsonify, request
from services.categoria_service import CategoriaService
from repositories.categoria_repository import CategoriaRepository

categoria_bp = Blueprint('categoria_bp', __name__)
categoria_service = CategoriaService(CategoriaRepository())

@categoria_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    categorias = categoria_service.get_all()
    return jsonify([categoria.to_dict() for categoria in categorias])

@categoria_bp.route('/categorias/<int:id>', methods=['GET'])
def obtener_categoria(id):
    categoria = categoria_service.get_by_id(id)
    if categoria:
        return jsonify(categoria.to_dict())
    return jsonify({"error": "Categoría no encontrada"}), 404

@categoria_bp.route('/categorias', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    categoria = categoria_service.create(data)
    return jsonify(categoria.to_dict()), 201

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    data = request.get_json()
    categoria = categoria_service.update(id, data)
    if categoria:
        return jsonify(categoria.to_dict())
    return jsonify({"error": "Categoría no encontrada"}), 404

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    result = categoria_service.delete(id)
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result), 204
