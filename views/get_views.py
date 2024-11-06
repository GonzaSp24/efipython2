from flask import Blueprint, jsonify
from models import Equipo, Modelo, Categoria, Stock, Marca, Caracteristica, Accesorio, Proveedor

get_bp = Blueprint('get', __name__)

# Endpoint para obtener todos los Equipos
# En tu archivo de vistas GET, ajusta así:
@get_bp.route('/equipos', methods=['GET'])
def get_equipos():
    equipos = Equipo.query.filter_by(eliminado=False).all()  # Asegúrate de tener `eliminado=False` aquí
    return jsonify([equipo.to_dict() for equipo in equipos])

# Endpoint para obtener todos los Modelos
@get_bp.route('/modelos', methods=['GET'])
def get_modelos():
    modelos = Modelo.query.all()
    return jsonify([modelo.to_dict() for modelo in modelos])

# Endpoint para obtener todas las Categorías
@get_bp.route('/categorias', methods=['GET'])
def get_categorias():
    categorias = Categoria.query.all()
    return jsonify([categoria.to_dict() for categoria in categorias])
# Endpoint para obtener todos los Stocks
@get_bp.route('/stock', methods=['GET'])
def get_stock():
    stocks = Stock.query.all()
    return jsonify([stock.to_dict() for stock in stocks])

# Endpoint para obtener todas las Marcas
@get_bp.route('/marcas', methods=['GET'])
def get_marcas():
    marcas = Marca.query.all()
    return jsonify([marca.to_dict() for marca in marcas])

# Endpoint para obtener todas las Características
@get_bp.route('/caracteristicas', methods=['GET'])
def get_caracteristicas():
    caracteristicas = Caracteristica.query.all()
    return jsonify([caracteristica.to_dict() for caracteristica in caracteristicas])

# Endpoint para obtener todos los Accesorios
@get_bp.route('/accesorios', methods=['GET'])
def get_accesorios():
    accesorios = Accesorio.query.all()
    return jsonify([accesorio.to_dict() for accesorio in accesorios])

# Endpoint para obtener todos los Proveedores
@get_bp.route('/proveedores', methods=['GET'])
def get_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify([proveedor.to_dict() for proveedor in proveedores])
