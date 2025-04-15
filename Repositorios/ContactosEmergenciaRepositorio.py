import pyodbc
from Entidades.ContactoEmergencia import ContactoEmergencia
from Utilidades import Configuracion

class ContactosEmergenciaRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, usuario_id, nombre, telefono, relacion FROM contactos_emergencia;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                contacto = ContactoEmergencia(
                    id=elemento[0],
                    usuario_id=elemento[1],
                    nombre=elemento[2],
                    telefono=elemento[3],
                    relacion=elemento[4]
                )
                lista.append(contacto)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar contactos_emergencia:", str(ex))
            return []

    def Guardar(self, contacto: ContactoEmergencia) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO contactos_emergencia (usuario_id, nombre, telefono, relacion)
                VALUES (?, ?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           contacto.usuario_id,
                           contacto.nombre,
                           contacto.telefono,
                           contacto.relacion)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Contacto guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el contacto:", str(ex))
            return "Error al guardar el contacto"

    def Actualizar(self, contacto: ContactoEmergencia) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE contactos_emergencia
                SET usuario_id = ?, nombre = ?, telefono = ?, relacion = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           contacto.usuario_id,
                           contacto.nombre,
                           contacto.telefono,
                           contacto.relacion,
                           contacto.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Contacto con ID {contacto.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el contacto:", str(ex))
            return "Error al actualizar el contacto"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM contactos_emergencia WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Contacto con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el contacto:", str(ex))
            return "Error al eliminar el contacto"
