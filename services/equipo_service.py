from repositories.equipo_repository import EquipoRepository

class EquipoService:
    def __init__(self, equipo_repository: EquipoRepository):
        self._equipo_repository = equipo_repository

    def get_all(self):
        return self._equipo_repository.get_all()

    def get_by_id(self, id):
        return self._equipo_repository.get_by_id(id)

    def create(self, data):
        return self._equipo_repository.create(data)

    def update(self, equipo_id, data):
        equipo = self.get_by_id(equipo_id)
        if equipo:
            return self._equipo_repository.update(equipo, data)
        return None

    def delete(self, equipo_id):
        equipo = self.get_by_id(equipo_id)
        if equipo:
            self._equipo_repository.delete(equipo)
            return {"message": "Equipo eliminado exitosamente"}
        return {"error": "Equipo no encontrado"}
