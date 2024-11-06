from flask import Blueprint, jsonify, request
from services.equipo_service import EquipoService
from repositories.equipo_repository import EquipoRepository

equipo_bp = Blueprint('equipo_bp', __name__)
equipo_service = EquipoService(EquipoRepository())

@equipo_bp.route('/equipos', methods=['GET'])
def listar_equipos():
    equipos = equipo_service.get_all()
    return jsonify([equipo.to_dict() for equipo in equipos])

@equipo_bp.route('/equipos/<int:id>', methods=['GET'])
def obtener_equipo(id):
    equipo = equipo_service.get_by_id(id)
    if equipo:
        return jsonify(equipo.to_dict())
    return jsonify({"error": "Equipo no encontrado"}), 404

@equipo_bp.route('/equipos', methods=['POST'])
def crear_equipo():
    data = request.get_json()
    equipo = equipo_service.create(data)
    return jsonify(equipo.to_dict()), 201

@equipo_bp.route('/equipos/<int:id>', methods=['PUT'])
def actualizar_equipo(id):
    data = request.get_json()
    equipo = equipo_service.update(id, data)
    if equipo:
        return jsonify(equipo.to_dict())
    return jsonify({"error": "Equipo no encontrado"}), 404

@equipo_bp.route('/equipos/<int:id>', methods=['DELETE'])
def eliminar_equipo(id):
    result = equipo_service.delete(id)
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result), 204
