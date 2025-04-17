from datetime import datetime

class Notificacion:
    def __init__(self, id: int, usuario_id: int, mensaje: str, fecha_hora: datetime, leido: bool):
        self.id: int = id
        self.usuario_id: int = usuario_id
        self.mensaje: str = mensaje
        self.fecha_hora: datetime = fecha_hora
        self.leido: bool = leido

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_usuario_id(self, usuario_id: int): self.usuario_id = usuario_id
    def get_usuario_id(self) -> int: return self.usuario_id

    def set_mensaje(self, mensaje: str): self.mensaje = mensaje
    def get_mensaje(self) -> str: return self.mensaje

    def set_fecha_hora(self, fecha_hora: datetime): self.fecha_hora = fecha_hora
    def get_fecha_hora(self) -> datetime: return self.fecha_hora

    def set_leido(self, leido: bool): self.leido = leido
    def get_leido(self) -> bool: return self.leido

    def __str__(self) -> str:
        return (f"ID: {self.id}, Usuario ID: {self.usuario_id}, Mensaje: {self.mensaje}, "
                f"Fecha y Hora: {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}, Leído: {self.leido}")