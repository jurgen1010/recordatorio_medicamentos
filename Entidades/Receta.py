class Receta:
    def __init__(self, id: int, usuario_id: int, doctor_id: int, fecha: str):
        self.id = id
        self.usuario_id = usuario_id
        self.doctor_id = doctor_id
        self.fecha = fecha

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_usuario_id(self, usuario_id: int): self.usuario_id = usuario_id
    def get_usuario_id(self) -> int: return self.usuario_id

    def set_doctor_id(self, doctor_id: int): self.doctor_id = doctor_id
    def get_doctor_id(self) -> int: return self.doctor_id

    def set_fecha(self, fecha: str): self.fecha = fecha
    def get_fecha(self) -> str: return self.fecha

    def __str__(self) -> str:
        return f"ID: {self.id}, UsuarioID: {self.usuario_id}, DoctorID: {self.doctor_id}, Fecha: {self.fecha}"
