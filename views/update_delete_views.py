from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from app import db
from models import Equipo, Modelo, Categoria, Stock, Marca, Caracteristica, Accesorio, Proveedor

update_delete_bp = Blueprint('update_delete', __name__)

# Endpoint para actualizar y hacer soft delete de un Equipo
@update_delete_bp.route('/equipos/<int:id>', methods=['PUT', 'DELETE'])
@jwt_required()
def update_delete_equipo(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar o eliminar equipos"}), 403

    equipo = Equipo.query.get_or_404(id)

    if request.method == 'PUT':
        data = request.get_json()
        equipo.nombre = data.get('nombre', equipo.nombre)
        equipo.modelo_id = data.get('modelo_id', equipo.modelo_id)
        equipo.categoria_id = data.get('categoria_id', equipo.categoria_id)
        equipo.costo = data.get('costo', equipo.costo)
        equipo.stock_id = data.get('stock_id', equipo.stock_id)
        equipo.marca_id = data.get('marca_id', equipo.marca_id)
        db.session.commit()
        return jsonify({"Mensaje": "Equipo actualizado correctamente", "Equipo": equipo.to_dict()}), 200

    elif request.method == 'DELETE':
        equipo.eliminado = True  # Soft delete al cambiar el estado de "eliminado" a True
        db.session.commit()
        return jsonify({"Mensaje": "Equipo marcado como eliminado (soft delete)"}), 200

# Endpoint para actualizar un Modelo
@update_delete_bp.route('/modelos/<int:id>', methods=['PUT'])
@jwt_required()
def update_modelo(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar modelos"}), 403

    modelo = Modelo.query.get_or_404(id)

    data = request.get_json()
    modelo.nombre = data.get('nombre', modelo.nombre)
    modelo.fabricante_id = data.get('fabricante_id', modelo.fabricante_id)
    db.session.commit()
    return jsonify({"Mensaje": "Modelo actualizado correctamente", "Modelo": modelo.to_dict()}), 200

# Endpoint para actualizar una Categoría
@update_delete_bp.route('/categorias/<int:id>', methods=['PUT'])
@jwt_required()
def update_categoria(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar categorías"}), 403

    categoria = Categoria.query.get_or_404(id)

    data = request.get_json()
    categoria.nombre = data.get('nombre', categoria.nombre)
    db.session.commit()
    return jsonify({"Mensaje": "Categoría actualizada correctamente", "Categoria": categoria.to_dict()}), 200

# Endpoint para actualizar un Stock
@update_delete_bp.route('/stock/<int:id>', methods=['PUT'])
@jwt_required()
def update_stock(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar stock"}), 403

    stock = Stock.query.get_or_404(id)

    data = request.get_json()
    stock.cantidad = data.get('cantidad', stock.cantidad)
    stock.ubicacion = data.get('ubicacion', stock.ubicacion)
    db.session.commit()
    return jsonify({"Mensaje": "Stock actualizado correctamente", "Stock": stock.to_dict()}), 200

# Endpoint para actualizar una Marca
@update_delete_bp.route('/marcas/<int:id>', methods=['PUT'])
@jwt_required()
def update_marca(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar marcas"}), 403

    marca = Marca.query.get_or_404(id)

    data = request.get_json()
    marca.nombre = data.get('nombre', marca.nombre)
    db.session.commit()
    return jsonify({"Mensaje": "Marca actualizada correctamente", "Marca": marca.to_dict()}), 200

# Endpoint para actualizar una Característica
@update_delete_bp.route('/caracteristicas/<int:id>', methods=['PUT'])
@jwt_required()
def update_caracteristica(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar características"}), 403

    caracteristica = Caracteristica.query.get_or_404(id)

    data = request.get_json()
    caracteristica.tipo = data.get('tipo', caracteristica.tipo)
    caracteristica.descripcion = data.get('descripcion', caracteristica.descripcion)
    db.session.commit()
    return jsonify({"Mensaje": "Característica actualizada correctamente", "Caracteristica": caracteristica.to_dict()}), 200

# Endpoint para actualizar un Accesorio
@update_delete_bp.route('/accesorios/<int:id>', methods=['PUT'])
@jwt_required()
def update_accesorio(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar accesorios"}), 403

    accesorio = Accesorio.query.get_or_404(id)

    data = request.get_json()
    accesorio.tipo = data.get('tipo', accesorio.tipo)
    accesorio.compatible_con = data.get('compatible_con', accesorio.compatible_con)
    accesorio.proveedor_id = data.get('proveedor_id', accesorio.proveedor_id)
    db.session.commit()
    return jsonify({"Mensaje": "Accesorio actualizado correctamente", "Accesorio": accesorio.to_dict()}), 200

# Endpoint para actualizar un Proveedor
@update_delete_bp.route('/proveedores/<int:id>', methods=['PUT'])
@jwt_required()
def update_proveedor(id):
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden modificar proveedores"}), 403

    proveedor = Proveedor.query.get_or_404(id)

    data = request.get_json()
    proveedor.nombre = data.get('nombre', proveedor.nombre)
    proveedor.contacto = data.get('contacto', proveedor.contacto)
    db.session.commit()
    return jsonify({"Mensaje": "Proveedor actualizado correctamente", "Proveedor": proveedor.to_dict()}), 200
