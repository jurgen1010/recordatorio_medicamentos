class Medicamento:
    def __init__(self, id: int, nombre: str, dosis: str, duracion: int, usuario_id: int, categoria_id: int = None):
        self.id: int = id
        self.nombre: str = nombre
        self.dosis: str = dosis
        self.duracion: int = duracion
        self.usuario_id: int = usuario_id
        self.categoria_id: int = categoria_id

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_nombre(self, nombre: str): self.nombre = nombre
    def get_nombre(self) -> str: return self.nombre

    def set_dosis(self, dosis: str): self.dosis = dosis
    def get_dosis(self) -> str: return self.dosis

    def set_duracion(self, duracion: int): self.duracion = duracion
    def get_duracion(self) -> int: return self.duracion

    def set_usuario_id(self, uid: int): self.usuario_id = uid
    def get_usuario_id(self) -> int: return self.usuario_id

    def set_categoria_id(self, cid: int): self.categoria_id = cid
    def get_categoria_id(self) -> int: return self.categoria_id

    def __str__(self) -> str:
        return (f"ID: {self.id}, Nombre: {self.nombre}, Dosis: {self.dosis}, "
                f"Duración: {self.duracion} días, Usuario ID: {self.usuario_id}, "
                f"Categoría ID: {self.categoria_id}")