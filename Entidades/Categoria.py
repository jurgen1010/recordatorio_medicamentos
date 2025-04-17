class Categoria:
    def __init__(self, id: int, nombre: str):
        self.id: int = id
        self.nombre: str = nombre

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_nombre(self, nombre: str): self.nombre = nombre
    def get_nombre(self) -> str: return self.nombre

    def __str__(self) -> str:
        return f"ID: {self.id}, Nombre: {self.nombre}"