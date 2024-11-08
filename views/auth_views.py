from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from app import db
from models import User
from schemas import UserSchema

auth_bp = Blueprint('auth', __name__)

# Endpoint de Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password = data.password

    # Busca al usuario en la base de datos
    usuario = User.query.filter_by(username=username).first()
    
    if usuario and check_password_hash(usuario.password_hash, password):
        # Crea el token de acceso con un reclamo adicional para saber si es admin
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=20),
            additional_claims={"administrador": usuario.is_admin}
        )
        return jsonify({'Token': f'Bearer {access_token}'})

    return jsonify({"Mensaje": "El usuario y la contraseña no coinciden"}), 401

# Endpoint para Crear Usuarios (solo administradores)
@auth_bp.route('/users', methods=['POST'])
@jwt_required()  # Solo permite el acceso a usuarios autenticados
def crear_usuario():
    additional_data = get_jwt()
    
    # Verificar si el usuario actual es administrador
    if not additional_data.get('administrador'):
        return jsonify({"Mensaje": "Solo los administradores pueden crear usuarios"}), 403
    
    # Obtener datos del request
    data = request.get_json()
    username = data.get('usuario')
    password = data.get('password')
    is_admin = data.get('is_admin', False)

    # Validar que username y password estén presentes
    if not username or not password:
        return jsonify({"Mensaje": "El nombre de usuario y la contraseña son requeridos"}), 400

    # Crear el nuevo usuario con contraseña cifrada
    nuevo_usuario = User(
        username=username,
        password_hash=generate_password_hash(password),
        is_admin=is_admin
    )
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "Mensaje": "Usuario creado correctamente",
        "Usuario": UserSchema().dump(nuevo_usuario)
    }), 201

# Endpoint para Obtener Usuarios (solo administradores)
@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def obtener_usuarios():
    additional_data = get_jwt()
    
    # Verificar si el usuario actual es administrador
    if not additional_data.get('administrador'):
        print("Acceso denegado: El usuario no es administrador")
        return jsonify({"Mensaje": "Solo los administradores pueden ver usuarios"}), 403

    try:
        print("Obteniendo lista de usuarios...")
        usuarios = User.query.all()
        if not usuarios:
            print("No se encontraron usuarios en la base de datos")
            return jsonify({"Mensaje": "No se encontraron usuarios"}), 404

        usuarios_data = UserSchema(many=True).dump(usuarios)
        print("Usuarios encontrados:", usuarios_data)
        return jsonify(usuarios_data), 200

    except Exception as e:
        print("Error al obtener los usuarios:", e)
        return jsonify({"Mensaje": "Error al obtener los usuarios"}), 400
