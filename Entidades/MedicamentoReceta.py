class MedicamentoReceta:
    def __init__(self, id: int, receta_id: int, medicamento_id: int):
        self.id = id
        self.receta_id = receta_id
        self.medicamento_id = medicamento_id

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_receta_id(self, receta_id: int): self.receta_id = receta_id
    def get_receta_id(self) -> int: return self.receta_id

    def set_medicamento_id(self, medicamento_id: int): self.medicamento_id = medicamento_id
    def get_medicamento_id(self) -> int: return self.medicamento_id

    def __str__(self) -> str:
        return f"ID: {self.id}, RecetaID: {self.receta_id}, MedicamentoID: {self.medicamento_id}"
