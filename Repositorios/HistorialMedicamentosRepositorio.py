import pyodbc
from Entidades.HistorialMedicamento import HistorialMedicamento
from Utilidades import Configuracion

class HistorialMedicamentosRepositorio:

    def Listar(self) -> list:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, usuario_id, medicamento_id, fecha_hora
                FROM historial_medicamentos;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:
                # Crear una instancia de HistorialMedicamento con los datos obtenidos
                historial = HistorialMedicamento(
                    id=elemento[0],
                    usuario_id=elemento[1],
                    medicamento_id=elemento[2],
                    fecha_hora=elemento[3]
                )
                lista.append(historial)

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return lista
        except Exception as ex:
            print("Error al listar historial de medicamentos:", str(ex))
            return []

    def Guardar(self, historial: HistorialMedicamento) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO historial_medicamentos (usuario_id, medicamento_id, fecha_hora)
                VALUES (?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           historial.usuario_id, 
                           historial.medicamento_id, 
                           historial.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'))  # Convertir datetime a string
            
            # Obtener el ID del último registro insertado
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Historial de medicamento guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el historial de medicamento:", str(ex))
            return "Error al guardar el historial de medicamento"

    def Actualizar(self, historial: HistorialMedicamento) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE historial_medicamentos
                SET usuario_id = ?, medicamento_id = ?, fecha_hora = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           historial.usuario_id, 
                           historial.medicamento_id, 
                           historial.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),  # Convertir datetime a string
                           historial.id)
                        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Historial de medicamento con ID {historial.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el historial de medicamento:", str(ex))
            return "Error al actualizar el historial de medicamento"

    def Eliminar(self, id: int) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM historial_medicamentos
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
                        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Historial de medicamento con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el historial de medicamento:", str(ex))
            return "Error al eliminar el historial de medicamento"