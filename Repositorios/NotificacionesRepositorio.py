import pyodbc
from Entidades.Notificacion import Notificacion
from Utilidades import Configuracion

class NotificacionesRepositorio:

    def Listar(self) -> list:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, usuario_id, mensaje, fecha_hora, leido
                FROM notificaciones;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:
                # Crear una instancia de Notificacion con los datos obtenidos
                notificacion = Notificacion(
                    id=elemento[0],
                    usuario_id=elemento[1],
                    mensaje=elemento[2],
                    fecha_hora=elemento[3],
                    leido=bool(elemento[4])
                )
                lista.append(notificacion)

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return lista
        except Exception as ex:
            print("Error al listar notificaciones:", str(ex))
            return []

    def Guardar(self, notificacion: Notificacion) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO notificaciones (usuario_id, mensaje, fecha_hora, leido)
                VALUES (?, ?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           notificacion.usuario_id, 
                           notificacion.mensaje, 
                           notificacion.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),  # Convertir datetime a string
                           notificacion.leido)
            
            # Obtener el ID del último registro insertado
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Notificación guardada exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar la notificación:", str(ex))
            return "Error al guardar la notificación"

    def Actualizar(self, notificacion: Notificacion) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE notificaciones
                SET usuario_id = ?, mensaje = ?, fecha_hora = ?, leido = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           notificacion.usuario_id, 
                           notificacion.mensaje, 
                           notificacion.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),  # Convertir datetime a string
                           notificacion.leido, 
                           notificacion.id)
                    
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Notificación con ID {notificacion.id} actualizada exitosamente"
        except Exception as ex:
            print("Error al actualizar la notificación:", str(ex))
            return "Error al actualizar la notificación"

    def Eliminar(self, id: int) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM notificaciones
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
                    
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Notificación con ID {id} eliminada exitosamente"
        except Exception as ex:
            print("Error al eliminar la notificación:", str(ex))
            return "Error al eliminar la notificación"