import pyodbc
from Entidades.HorarioMedicamento import HorarioMedicamento
from Utilidades import Configuracion

class HorariosMedicamentosRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, medicamento_id, hora FROM horarios_medicamentos;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                horario = HorarioMedicamento(
                    id=elemento[0],
                    medicamento_id=elemento[1],
                    hora=str(elemento[2])
                )
                lista.append(horario)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar horarios_medicamentos:", str(ex))
            return []

    def Guardar(self, horario: HorarioMedicamento) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO horarios_medicamentos (medicamento_id, hora)
                VALUES (?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, horario.medicamento_id, horario.hora)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Horario guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el horario:", str(ex))
            return "Error al guardar el horario"

    def Actualizar(self, horario: HorarioMedicamento) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE horarios_medicamentos
                SET medicamento_id = ?, hora = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           horario.medicamento_id,
                           horario.hora,
                           horario.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Horario con ID {horario.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el horario:", str(ex))
            return "Error al actualizar el horario"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM horarios_medicamentos WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Horario con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el horario:", str(ex))
            return "Error al eliminar el horario"
