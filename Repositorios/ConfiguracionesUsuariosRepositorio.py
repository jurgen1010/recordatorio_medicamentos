import pyodbc
from Entidades.ConfiguracionUsuario import ConfiguracionUsuario
from Utilidades import Configuracion

class ConfiguracionesUsuariosRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, usuario_id, recibir_notificaciones, zona_horaria FROM configuraciones_usuarios;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                config = ConfiguracionUsuario(
                    id=elemento[0],
                    usuario_id=elemento[1],
                    recibir_notificaciones=bool(elemento[2]),
                    zona_horaria=elemento[3]
                )
                lista.append(config)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar configuraciones_usuarios:", str(ex))
            return []

    def Guardar(self, configuracion_usuario: ConfiguracionUsuario) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO configuraciones_usuarios (usuario_id, recibir_notificaciones, zona_horaria)
                VALUES (?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           configuracion_usuario.usuario_id,
                           configuracion_usuario.recibir_notificaciones,
                           configuracion_usuario.zona_horaria)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Configuración guardada exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar la configuración:", str(ex))
            return "Error al guardar la configuración"

    def Actualizar(self, configuracion_usuario: ConfiguracionUsuario) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE configuraciones_usuarios
                SET usuario_id = ?, recibir_notificaciones = ?, zona_horaria = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           configuracion_usuario.usuario_id,
                           configuracion_usuario.recibir_notificaciones,
                           configuracion_usuario.zona_horaria,
                           configuracion_usuario.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Configuración con ID {configuracion_usuario.id} actualizada exitosamente"
        except Exception as ex:
            print("Error al actualizar la configuración:", str(ex))
            return "Error al actualizar la configuración"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM configuraciones_usuarios WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Configuración con ID {id} eliminada exitosamente"
        except Exception as ex:
            print("Error al eliminar la configuración:", str(ex))
            return "Error al eliminar la configuración"
