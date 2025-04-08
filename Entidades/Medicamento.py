class Medicamento:
    def __init__(self):
        self.id = None
        self.nombre = ""
        self.dosis = ""
        self.frecuencia = 0
        self.horario_inicio = None
        self.duracion = 0
        self.usuario_id = None

    def set_id(self, id): self.id = id
    def get_id(self): return self.id

    def set_nombre(self, nombre): self.nombre = nombre
    def get_nombre(self): return self.nombre

    def set_dosis(self, dosis): self.dosis = dosis
    def get_dosis(self): return self.dosis

    def set_frecuencia(self, frecuencia): self.frecuencia = frecuencia
    def get_frecuencia(self): return self.frecuencia

    def set_horario_inicio(self, horario): self.horario_inicio = horario
    def get_horario_inicio(self): return self.horario_inicio

    def set_duracion(self, duracion): self.duracion = duracion
    def get_duracion(self): return self.duracion

    def set_usuario_id(self, uid): self.usuario_id = uid
    def get_usuario_id(self): return self.usuario_id
