class HorarioMedicamento:
    def __init__(self, id: int, medicamento_id: int, hora: str):
        self.id = id
        self.medicamento_id = medicamento_id
        self.hora = hora

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_medicamento_id(self, medicamento_id: int): self.medicamento_id = medicamento_id
    def get_medicamento_id(self) -> int: return self.medicamento_id

    def set_hora(self, hora: str): self.hora = hora
    def get_hora(self) -> str: return self.hora

    def __str__(self) -> str:
        return f"ID: {self.id}, MedicamentoID: {self.medicamento_id}, Hora: {self.hora}"
