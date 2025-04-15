import pyodbc
from Entidades.MedicamentoReceta import MedicamentoReceta
from Utilidades import Configuracion

class MedicamentosRecetasRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, receta_id, medicamento_id FROM medicamentos_recetas;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                item = MedicamentoReceta(
                    id=elemento[0],
                    receta_id=elemento[1],
                    medicamento_id=elemento[2]
                )
                lista.append(item)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar medicamentos_recetas:", str(ex))
            return []

    def Guardar(self, medicamento_receta: MedicamentoReceta) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "INSERT INTO medicamentos_recetas (receta_id, medicamento_id) VALUES (?, ?);"
            cursor = conexion.cursor()
            cursor.execute(consulta, medicamento_receta.receta_id, medicamento_receta.medicamento_id)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Registro guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el medicamento_receta:", str(ex))
            return "Error al guardar el registro"

    def Actualizar(self, medicamento_receta: MedicamentoReceta) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE medicamentos_recetas
                SET receta_id = ?, medicamento_id = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           medicamento_receta.receta_id,
                           medicamento_receta.medicamento_id,
                           medicamento_receta.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Registro con ID {medicamento_receta.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el registro:", str(ex))
            return "Error al actualizar el registro"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM medicamentos_recetas WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Registro con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el registro:", str(ex))
            return "Error al eliminar el registro"
