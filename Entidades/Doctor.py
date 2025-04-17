class Doctor:
    def __init__(self, id: int, nombre: str, especialidad: str, telefono: str, correo: str):
        self.id: int = id
        self.nombre: str = nombre
        self.especialidad: str = especialidad
        self.telefono: str = telefono
        self.correo: str = correo

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_nombre(self, nombre: str): self.nombre = nombre
    def get_nombre(self) -> str: return self.nombre

    def set_especialidad(self, especialidad: str): self.especialidad = especialidad
    def get_especialidad(self) -> str: return self.especialidad

    def set_telefono(self, telefono: str): self.telefono = telefono
    def get_telefono(self) -> str: return self.telefono

    def set_correo(self, correo: str): self.correo = correo
    def get_correo(self) -> str: return self.correo

    def __str__(self) -> str:
        return (f"ID: {self.id}, Nombre: {self.nombre}, Especialidad: {self.especialidad}, "
                f"Teléfono: {self.telefono}, Correo: {self.correo}")