from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    eliminado = db.Column(db.Boolean, default=False)

    modelo_relacionado = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    categoria_relacionado = db.relationship('Categoria', backref=db.backref('equipos', lazy=True))
    stock_relacionado = db.relationship('Stock', backref=db.backref('equipos', lazy=True))
    marca_relacionado = db.relationship('Marca', backref=db.backref('equipos', lazy=True))

    caracteristicas = db.relationship(
        'Caracteristica', 
        secondary='equipo_caracteristicas', 
        backref=db.backref('equipos_relacionados', lazy=True), 
        overlaps="caracteristicas_relacionadas,equipos_relacionados"
    )
    accesorios = db.relationship('Accesorio', secondary='equipo_accesorios', backref=db.backref('equipos', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo_id": self.modelo_id,
            "categoria_id": self.categoria_id,
            "costo": self.costo,
            "stock_id": self.stock_id,
            "marca_id": self.marca_id,
            "eliminado": self.eliminado,
        }

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "descripcion": self.descripcion
        }

class EquipoCaracteristicas(db.Model):
    __tablename__ = 'equipo_caracteristicas'
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), primary_key=True)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), primary_key=True)

class EquipoAccesorios(db.Model):
    __tablename__ = 'equipo_accesorios'
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), primary_key=True)
    accesorio_id = db.Column(db.Integer, db.ForeignKey('accesorio.id'), primary_key=True)

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fabricante_id": self.fabricante_id
        }

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "pais_origen": self.pais_origen
        }

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "ubicacion": self.ubicacion
        }

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    contacto = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "contacto": self.contacto
        }

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    compatible_con = db.Column(db.String(50))
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "compatible_con": self.compatible_con,
            "proveedor_id": self.proveedor_id
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "is_admin": self.is_admin
        }
