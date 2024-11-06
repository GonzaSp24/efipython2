from app import ma
from marshmallow import validates, ValidationError, fields
from models import User, Marca, Equipo, Modelo, Categoria

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class UserMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field()

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca  # Define el modelo aquí para asegurar el mapeo

    id = ma.auto_field()
    nombre = ma.auto_field()

class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo

    id = ma.auto_field()
    nombre = ma.auto_field()

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

    id = ma.auto_field()
    nombre = ma.auto_field()

class EquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo

    id = ma.auto_field()
    nombre = ma.auto_field()
    modelo_id = ma.auto_field()
    categoria_id = ma.auto_field()
    costo = ma.auto_field()
    stock_id = ma.auto_field()
    marca_id = ma.auto_field()
    eliminado = ma.auto_field()

    # Anidando `MarcaSchema`, `ModeloSchema`, y `CategoriaSchema`
    marca = fields.Nested(MarcaSchema)
    modelo = fields.Nested(ModeloSchema)
    categoria = fields.Nested(CategoriaSchema)

    @validates('costo')
    def validate_costo(self, value):
        if value < 0:
            raise ValidationError("El costo no puede ser negativo.")
