from app import db
from models import Modelo

class ModeloRepository:
    def get_all(self):
        return Modelo.query.all()

    def get_by_id(self, id):
        return Modelo.query.get(id)

    def create(self, data):
        modelo = Modelo(**data)
        db.session.add(modelo)
        db.session.commit()
        return modelo

    def update(self, modelo, data):
        for key, value in data.items():
            setattr(modelo, key, value)
        db.session.commit()
        return modelo

    def delete(self, modelo):
        db.session.delete(modelo)
        db.session.commit()
