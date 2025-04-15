class ContactoEmergencia:
    def __init__(self, id: int, usuario_id: int, nombre: str, telefono: str, relacion: str):
        self.id = id
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.telefono = telefono
        self.relacion = relacion

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_usuario_id(self, usuario_id: int): self.usuario_id = usuario_id
    def get_usuario_id(self) -> int: return self.usuario_id

    def set_nombre(self, nombre: str): self.nombre = nombre
    def get_nombre(self) -> str: return self.nombre

    def set_telefono(self, telefono: str): self.telefono = telefono
    def get_telefono(self) -> str: return self.telefono

    def set_relacion(self, relacion: str): self.relacion = relacion
    def get_relacion(self) -> str: return self.relacion

    def __str__(self) -> str:
        return f"ID: {self.id}, UsuarioID: {self.usuario_id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Relación: {self.relacion}"
