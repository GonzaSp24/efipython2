from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from werkzeug.security import generate_password_hash
from app import db
from models import Equipo, Modelo, Categoria, Stock, Marca, Caracteristica, Accesorio, Proveedor

create_bp = Blueprint('create', __name__)

# Endpoint para crear un nuevo Equipo
@create_bp.route('/equipos', methods=['POST'])
@jwt_required()
def create_equipo():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear equipos"}), 403

    data = request.get_json()
    nuevo_equipo = Equipo(
        nombre=data.get('nombre'),
        modelo_id=data.get('modelo_id'),
        categoria_id=data.get('categoria_id'),
        costo=data.get('costo'),
        stock_id=data.get('stock_id'),
        marca_id=data.get('marca_id')
    )
    db.session.add(nuevo_equipo)
    db.session.commit()
    return jsonify({"Mensaje": "Equipo creado correctamente", "Equipo": nuevo_equipo.to_dict()}), 201

# Repite esta estructura para otros modelos:

@create_bp.route('/modelos', methods=['POST'])
@jwt_required()
def create_modelo():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear modelos"}), 403

    data = request.get_json()
    nuevo_modelo = Modelo(
        nombre=data.get('nombre'),
        fabricante_id=data.get('fabricante_id')
    )
    db.session.add(nuevo_modelo)
    db.session.commit()
    return jsonify({"Mensaje": "Modelo creado correctamente", "Modelo": nuevo_modelo.to_dict()}), 201

# Endpoint para crear una nueva Categoría
@create_bp.route('/categorias', methods=['POST'])
@jwt_required()
def create_categoria():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear categorías"}), 403

    data = request.get_json()
    nueva_categoria = Categoria(
        nombre=data.get('nombre')
    )
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({"Mensaje": "Categoría creada correctamente", "Categoria": nueva_categoria.to_dict()}), 201


# Endpoint para crear un nuevo Stock
@create_bp.route('/stock', methods=['POST'])
@jwt_required()
def create_stock():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear stock"}), 403

    data = request.get_json()
    nuevo_stock = Stock(
        cantidad=data.get('cantidad'),
        ubicacion=data.get('ubicacion')
    )
    db.session.add(nuevo_stock)
    db.session.commit()
    return jsonify({"Mensaje": "Stock creado correctamente", "Stock": nuevo_stock.to_dict()}), 201


# Endpoint para crear una nueva Marca
@create_bp.route('/marcas', methods=['POST'])
@jwt_required()
def create_marca():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear marcas"}), 403

    data = request.get_json()
    nueva_marca = Marca(
        nombre=data.get('nombre')
    )
    db.session.add(nueva_marca)
    db.session.commit()
    return jsonify({"Mensaje": "Marca creada correctamente", "Marca": nueva_marca.to_dict()}), 201


# Endpoint para crear una nueva Caracteristica
@create_bp.route('/caracteristicas', methods=['POST'])
@jwt_required()
def create_caracteristica():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear características"}), 403

    data = request.get_json()
    nueva_caracteristica = Caracteristica(
        tipo=data.get('tipo'),
        descripcion=data.get('descripcion')
    )
    db.session.add(nueva_caracteristica)
    db.session.commit()
    return jsonify({"Mensaje": "Característica creada correctamente", "Caracteristica": nueva_caracteristica.to_dict()}), 201


# Endpoint para crear un nuevo Accesorio
@create_bp.route('/accesorios', methods=['POST'])
@jwt_required()
def create_accesorio():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear accesorios"}), 403

    data = request.get_json()
    nuevo_accesorio = Accesorio(
        tipo=data.get('tipo'),
        compatible_con=data.get('compatible_con'),
        proveedor_id=data.get('proveedor_id')
    )
    db.session.add(nuevo_accesorio)
    db.session.commit()
    return jsonify({"Mensaje": "Accesorio creado correctamente", "Accesorio": nuevo_accesorio.to_dict()}), 201


# Endpoint para crear un nuevo Proveedor
@create_bp.route('/proveedores', methods=['POST'])
@jwt_required()
def create_proveedor():
    additional_data = get_jwt()
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear proveedores"}), 403

    data = request.get_json()
    nuevo_proveedor = Proveedor(
        nombre=data.get('nombre'),
        contacto=data.get('contacto')
    )
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return jsonify({"Mensaje": "Proveedor creado correctamente", "Proveedor": nuevo_proveedor.to_dict()}), 201
