class Medicamento:
    def __init__(self, id, nombre, dosis, duracion, usuario_id, categoria_id=None):
        self.id = id
        self.nombre = nombre
        self.dosis = dosis
        self.duracion = duracion
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id

    def set_id(self, id): self.id = id
    def get_id(self): return self.id

    def set_nombre(self, nombre): self.nombre = nombre
    def get_nombre(self): return self.nombre

    def set_dosis(self, dosis): self.dosis = dosis
    def get_dosis(self): return self.dosis

    def set_duracion(self, duracion): self.duracion = duracion
    def get_duracion(self): return self.duracion

    def set_usuario_id(self, uid): self.usuario_id = uid
    def get_usuario_id(self): return self.usuario_id

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Dosis: {self.dosis}, "
               f"Duración: {self.duracion} días, Usuario ID: {self.usuario_id}, "
               f"Categoría ID: {self.categoria_id}")