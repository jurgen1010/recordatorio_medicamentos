class ConfiguracionUsuario:
    def __init__(self, id: int, usuario_id: int, recibir_notificaciones: bool = True, zona_horaria: str = 'UTC'):
        self.id = id
        self.usuario_id = usuario_id
        self.recibir_notificaciones = recibir_notificaciones
        self.zona_horaria = zona_horaria

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_usuario_id(self, usuario_id: int): self.usuario_id = usuario_id
    def get_usuario_id(self) -> int: return self.usuario_id

    def set_recibir_notificaciones(self, recibir_notificaciones: bool): self.recibir_notificaciones = recibir_notificaciones
    def get_recibir_notificaciones(self) -> bool: return self.recibir_notificaciones

    def set_zona_horaria(self, zona_horaria: str): self.zona_horaria = zona_horaria
    def get_zona_horaria(self) -> str: return self.zona_horaria

    def __str__(self) -> str:
        return f"ID: {self.id}, UsuarioID: {self.usuario_id}, Notificaciones: {self.recibir_notificaciones}, Zona Horaria: {self.zona_horaria}"
