import pyodbc
from Entidades.Doctor import Doctor
from Utilidades import Configuracion

class DoctoresRepositorio:

    def Listar(self) -> list:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, nombre, especialidad, telefono, correo
                FROM doctores;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:
                # Crear una instancia de Doctor con los datos obtenidos
                doctor = Doctor(
                    id=elemento[0],
                    nombre=elemento[1],
                    especialidad=elemento[2],
                    telefono=elemento[3],
                    correo=elemento[4]
                )
                lista.append(doctor)

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return lista
        except Exception as ex:
            print("Error al listar doctores:", str(ex))
            return []

    def Guardar(self, doctor: Doctor) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            
            # Verificar si el correo ya existe
            consulta_verificar = """
                SELECT COUNT(*) FROM doctores WHERE correo = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta_verificar, doctor.correo)
            if cursor.fetchone()[0] > 0:
                return f"Error: El correo '{doctor.correo}' ya está registrado."

            consulta = """
                INSERT INTO doctores (nombre, especialidad, telefono, correo)
                VALUES (?, ?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           doctor.nombre, 
                           doctor.especialidad, 
                           doctor.telefono, 
                           doctor.correo)
            
            # Obtener el ID del último registro insertado
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Doctor guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el doctor:", str(ex))
            return "Error al guardar el doctor"

    def Actualizar(self, doctor: Doctor) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)

            # Verificar si el correo ya existe en otro registro
            consulta_verificar = """
                SELECT COUNT(*) FROM doctores WHERE correo = ? AND id != ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta_verificar, doctor.correo, doctor.id)
            if cursor.fetchone()[0] > 0:
                return f"Error: El correo '{doctor.correo}' ya está registrado por otro doctor."

            consulta = """
                UPDATE doctores
                SET nombre = ?, especialidad = ?, telefono = ?, correo = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           doctor.nombre, 
                           doctor.especialidad, 
                           doctor.telefono, 
                           doctor.correo, 
                           doctor.id)
                        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Doctor con ID {doctor.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el doctor:", str(ex))
            return "Error al actualizar el doctor"

    def Eliminar(self, id: int) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM doctores
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
                        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Doctor con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el doctor:", str(ex))
            return "Error al eliminar el doctor"