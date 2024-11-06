from repositories.marca_repository import MarcaRepository

class MarcaService:
    def __init__(self, marca_repository: MarcaRepository):
        self._marca_repository = marca_repository

    def get_all(self):
        return self._marca_repository.get_all()

    def get_by_id(self, id):
        return self._marca_repository.get_by_id(id)

    def create(self, data):
        return self._marca_repository.create(data)

    def update(self, marca_id, data):
        marca = self.get_by_id(marca_id)
        if marca:
            return self._marca_repository.update(marca, data)
        return None

    def delete(self, marca_id):
        marca = self.get_by_id(marca_id)
        if marca:
            self._marca_repository.delete(marca)
            return {"message": "Marca eliminada exitosamente"}
        return {"error": "Marca no encontrada"}
