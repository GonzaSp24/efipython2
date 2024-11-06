from app import db
from models import Marca

class MarcaRepository:
    def get_all(self):
        return Marca.query.all()

    def get_by_id(self, id):
        return Marca.query.get(id)

    def create(self, data):
        marca = Marca(**data)
        db.session.add(marca)
        db.session.commit()
        return marca

    def update(self, marca, data):
        for key, value in data.items():
            setattr(marca, key, value)
        db.session.commit()
        return marca

    def delete(self, marca):
        db.session.delete(marca)
        db.session.commit()
