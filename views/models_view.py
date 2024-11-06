from flask import Blueprint, jsonify, request
from services.modelo_service import ModeloService
from repositories.modelo_repository import ModeloRepository

modelo_bp = Blueprint('modelo_bp', __name__)
modelo_service = ModeloService(ModeloRepository())

@modelo_bp.route('/modelos', methods=['GET'])
def listar_modelos():
    modelos = modelo_service.get_all()
    return jsonify([modelo.to_dict() for modelo in modelos])

@modelo_bp.route('/modelos/<int:id>', methods=['GET'])
def obtener_modelo(id):
    modelo = modelo_service.get_by_id(id)
    if modelo:
        return jsonify(modelo.to_dict())
    return jsonify({"error": "Modelo no encontrado"}), 404

@modelo_bp.route('/modelos', methods=['POST'])
def crear_modelo():
    data = request.get_json()
    modelo = modelo_service.create(data)
    return jsonify(modelo.to_dict()), 201

@modelo_bp.route('/modelos/<int:id>', methods=['PUT'])
def actualizar_modelo(id):
    data = request.get_json()
    modelo = modelo_service.update(id, data)
    if modelo:
        return jsonify(modelo.to_dict())
    return jsonify({"error": "Modelo no encontrado"}), 404

@modelo_bp.route('/modelos/<int:id>', methods=['DELETE'])
def eliminar_modelo(id):
    result = modelo_service.delete(id)
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result), 204
