from repositories.categoria_repository import CategoriaRepository

class CategoriaService:
    def __init__(self, categoria_repository: CategoriaRepository):
        self._categoria_repository = categoria_repository

    def get_all(self):
        return self._categoria_repository.get_all()

    def get_by_id(self, id):
        return self._categoria_repository.get_by_id(id)

    def create(self, data):
        return self._categoria_repository.create(data)

    def update(self, categoria_id, data):
        categoria = self.get_by_id(categoria_id)
        if categoria:
            return self._categoria_repository.update(categoria, data)
        return None

    def delete(self, categoria_id):
        categoria = self.get_by_id(categoria_id)
        if categoria:
            self._categoria_repository.delete(categoria)
            return {"message": "Categoría eliminada exitosamente"}
        return {"error": "Categoría no encontrada"}
