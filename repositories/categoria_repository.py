from app import db
from models import Categoria

class CategoriaRepository:
    def get_all(self):
        return Categoria.query.all()

    def get_by_id(self, id):
        return Categoria.query.get(id)

    def create(self, data):
        categoria = Categoria(**data)
        db.session.add(categoria)
        db.session.commit()
        return categoria

    def update(self, categoria, data):
        for key, value in data.items():
            setattr(categoria, key, value)
        db.session.commit()
        return categoria

    def delete(self, categoria):
        db.session.delete(categoria)
        db.session.commit()
