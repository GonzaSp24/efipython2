from app import db
from models import Equipo

class EquipoRepository:
    def get_all(self):
        return Equipo.query.all()

    def get_by_id(self, id):
        return Equipo.query.get(id)

    def create(self, data):
        equipo = Equipo(**data)
        db.session.add(equipo)
        db.session.commit()
        return equipo

    def update(self, equipo, data):
        for key, value in data.items():
            setattr(equipo, key, value)
        db.session.commit()
        return equipo

    def delete(self, equipo):
        db.session.delete(equipo)
        db.session.commit()
