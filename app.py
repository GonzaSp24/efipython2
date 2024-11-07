import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@db/{os.getenv('MYSQL_DATABASE')}"
)

# Configuración de otras variables
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Clave secreta para JWT

# Inicializar extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

# Importar modelos y vistas
from models import User, Equipo, Modelo, Marca, Categoria, Stock, Caracteristica, Accesorio
from views import register_bp
register_bp(app)  # Registrar los Blueprints

# Crear usuario administrador al iniciar la aplicación si no existe
if __name__ == '__main__':
    with app.app_context():
        if not User.query.filter_by(username="admin").first():
            admin = User(username="admin", password_hash=generate_password_hash("admin_password"), is_admin=True)
            db.session.add(admin)
            db.session.commit()
            print("Usuario administrador creado con éxito.")
    app.run(debug=True)
