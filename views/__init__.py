from .auth_views import auth_bp
from .equipos_view import equipo_bp
from .models_view import modelo_bp
from .categorias_view import categoria_bp
from .get_views import get_bp
from .create_views import create_bp 
from .update_delete_views import update_delete_bp
def register_bp(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(equipo_bp)
    app.register_blueprint(modelo_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(get_bp)  # Registrar los endpoints GET 
    app.register_blueprint(create_bp)  # Registrar los endpoints POST
    app.register_blueprint(update_delete_bp)
