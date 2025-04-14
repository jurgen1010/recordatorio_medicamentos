class Usuario:
    def __init__(self, id: int, nombre: str, correo: str, contraseña: str):
        self.id: int = id
        self.nombre: str = nombre
        self.correo: str = correo
        self.contraseña: str = contraseña

    
    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    
    def set_nombre(self, nombre: str): self.nombre = nombre
    def get_nombre(self) -> str: return self.nombre

    
    def set_correo(self, correo: str): self.correo = correo
    def get_correo(self) -> str: return self.correo

   
    def set_contraseña(self, contraseña: str): self.contraseña = contraseña
    def get_contraseña(self) -> str: return self.contraseña

    
    def __str__(self) -> str:
        return f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Contraseña: {self.contraseña}"