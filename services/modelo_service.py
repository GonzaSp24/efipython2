from repositories.modelo_repository import ModeloRepository

class ModeloService:
    def __init__(self, modelo_repository: ModeloRepository):
        self._modelo_repository = modelo_repository

    def get_all(self):
        return self._modelo_repository.get_all()

    def get_by_id(self, id):
        return self._modelo_repository.get_by_id(id)

    def create(self, data):
        return self._modelo_repository.create(data)

    def update(self, modelo_id, data):
        modelo = self.get_by_id(modelo_id)
        if modelo:
            return self._modelo_repository.update(modelo, data)
        return None

    def delete(self, modelo_id):
        modelo = self.get_by_id(modelo_id)
        if modelo:
            self._modelo_repository.delete(modelo)
            return {"message": "Modelo eliminado exitosamente"}
        return {"error": "Modelo no encontrado"}
