import pyodbc
from Entidades.Receta import Receta
from Utilidades import Configuracion

class RecetasRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, usuario_id, doctor_id, fecha FROM recetas;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                receta = Receta(
                    id=elemento[0],
                    usuario_id=elemento[1],
                    doctor_id=elemento[2],
                    fecha=str(elemento[3])
                )
                lista.append(receta)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar recetas:", str(ex))
            return []

    def Guardar(self, receta: Receta) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "INSERT INTO recetas (usuario_id, doctor_id, fecha) VALUES (?, ?, ?);"
            cursor = conexion.cursor()
            cursor.execute(consulta, receta.usuario_id, receta.doctor_id, receta.fecha)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Receta guardada exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar la receta:", str(ex))
            return "Error al guardar la receta"

    def Actualizar(self, receta: Receta) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "UPDATE recetas SET usuario_id = ?, doctor_id = ?, fecha = ? WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, receta.usuario_id, receta.doctor_id, receta.fecha, receta.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Receta con ID {receta.id} actualizada exitosamente"
        except Exception as ex:
            print("Error al actualizar la receta:", str(ex))
            return "Error al actualizar la receta"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM recetas WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Receta con ID {id} eliminada exitosamente"
        except Exception as ex:
            print("Error al eliminar la receta:", str(ex))
            return "Error al eliminar la receta"
