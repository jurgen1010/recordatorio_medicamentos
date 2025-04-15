class Farmacia:
    def __init__(self, id: int, nombre: str, direccion: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_nombre(self, nombre: str): self.nombre = nombre
    def get_nombre(self) -> str: return self.nombre

    def set_direccion(self, direccion: str): self.direccion = direccion
    def get_direccion(self) -> str: return self.direccion

    def set_telefono(self, telefono: str): self.telefono = telefono
    def get_telefono(self) -> str: return self.telefono

    def __str__(self) -> str:
        return f"ID: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
