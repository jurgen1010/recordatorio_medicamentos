from datetime import datetime

class Recordatorio:
    def __init__(self, id: int, medicamento_id: int, fecha_hora: datetime, estado: str):
        self.id: int = id
        self.medicamento_id: int = medicamento_id
        self.fecha_hora: datetime = fecha_hora  # Ahora es de tipo datetime
        self.estado: str = estado

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_medicamento_id(self, medicamento_id: int): self.medicamento_id = medicamento_id
    def get_medicamento_id(self) -> int: return self.medicamento_id

    def set_fecha_hora(self, fecha_hora: datetime): self.fecha_hora = fecha_hora
    def get_fecha_hora(self) -> datetime: return self.fecha_hora

    def set_estado(self, estado: str): self.estado = estado
    def get_estado(self) -> str: return self.estado

    def __str__(self) -> str:
        return (f"ID: {self.id}, Medicamento ID: {self.medicamento_id}, "
                f"Fecha y Hora: {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}, Estado: {self.estado}")