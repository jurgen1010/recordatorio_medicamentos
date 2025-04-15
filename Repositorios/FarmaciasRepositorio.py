import pyodbc
from Entidades.Farmacia import Farmacia
from Utilidades import Configuracion

class FarmaciasRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, nombre, direccion, telefono FROM farmacias;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                farmacia = Farmacia(
                    id=elemento[0],
                    nombre=elemento[1],
                    direccion=elemento[2],
                    telefono=elemento[3]
                )
                lista.append(farmacia)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar farmacias:", str(ex))
            return []

    def Guardar(self, farmacia: Farmacia) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "INSERT INTO farmacias (nombre, direccion, telefono) VALUES (?, ?, ?);"
            cursor = conexion.cursor()
            cursor.execute(consulta, farmacia.nombre, farmacia.direccion, farmacia.telefono)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Farmacia guardada exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar la farmacia:", str(ex))
            return "Error al guardar la farmacia"

    def Actualizar(self, farmacia: Farmacia) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE farmacias
                SET nombre = ?, direccion = ?, telefono = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, farmacia.nombre, farmacia.direccion, farmacia.telefono, farmacia.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Farmacia con ID {farmacia.id} actualizada exitosamente"
        except Exception as ex:
            print("Error al actualizar la farmacia:", str(ex))
            return "Error al actualizar la farmacia"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM farmacias WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Farmacia con ID {id} eliminada exitosamente"
        except Exception as ex:
            print("Error al eliminar la farmacia:", str(ex))
            return "Error al eliminar la farmacia"
