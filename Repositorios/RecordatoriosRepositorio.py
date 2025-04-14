import pyodbc
from Entidades.Recordatorio import Recordatorio
from Utilidades import Configuracion
from datetime import datetime

class RecordatoriosRepositorio:

    def Listar(self) -> list:
        try:       
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, medicamento_id, fecha_hora, estado
                FROM recordatorios;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:                                
                recordatorio = Recordatorio(
                    id=elemento[0],
                    medicamento_id=elemento[1],
                    fecha_hora=elemento[2],
                    estado=elemento[3]
                )
                lista.append(recordatorio)
            
            cursor.close()
            conexion.close()

            return lista
        except Exception as ex:
            print("Error al listar recordatorios:", str(ex))
            return []

    def Guardar(self, recordatorio: Recordatorio) -> str:
        try:
            # Conexión a la base de datos
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO recordatorios (medicamento_id, fecha_hora, estado)
                VALUES (?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                        recordatorio.medicamento_id, 
                        recordatorio.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),  # Convertir datetime a string
                        recordatorio.estado)
                    
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            
            conexion.commit()
            
            cursor.close()
            conexion.close()

            return f"Recordatorio guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el recordatorio:", str(ex))
            return "Error al guardar el recordatorio"

    def Actualizar(self, recordatorio: Recordatorio) -> str:
        try:
            # Conexión a la base de datos
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE recordatorios
                SET medicamento_id = ?, fecha_hora = ?, estado = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           recordatorio.medicamento_id, 
                           recordatorio.fecha_hora, 
                           recordatorio.estado, 
                           recordatorio.id)
            
            # Confirmar los cambios
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Recordatorio con ID {recordatorio.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el recordatorio:", str(ex))
            return "Error al actualizar el recordatorio"

    def Eliminar(self, id: int) -> str:
        try:
            # Conexión a la base de datos
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM recordatorios
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            
            # Confirmar los cambios
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Recordatorio con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el recordatorio:", str(ex))
            return "Error al eliminar el recordatorio"