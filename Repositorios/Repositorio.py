import pyodbc
from entidades.Medicamento import Medicamento
from config.Configuracion import Configuracion

class MedicamentosRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT id, nombre, dosis, frecuencia, horario_inicio, duracion, usuario_id
                FROM medicamentos;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for row in cursor:
                medicamento = Medicamento()
                medicamento.set_id(row[0])
                medicamento.set_nombre(row[1])
                medicamento.set_dosis(row[2])
                medicamento.set_frecuencia(row[3])
                medicamento.set_horario_inicio(row[4])
                medicamento.set_duracion(row[5])
                medicamento.set_usuario_id(row[6])
                lista.append(medicamento)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar medicamentos:", str(ex))
            return []

    def Agregar(self, medicamento: Medicamento) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO medicamentos (nombre, dosis, frecuencia, horario_inicio, duracion, usuario_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta,
                medicamento.get_nombre(),
                medicamento.get_dosis(),
                medicamento.get_frecuencia(),
                medicamento.get_horario_inicio(),
                medicamento.get_duracion(),
                medicamento.get_usuario_id()
            )

            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print("Error al agregar medicamento:", str(ex))
            return False

    def Eliminar(self, id_medicamento: int) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM medicamentos WHERE id = ?"
            cursor.execute(consulta, id_medicamento)

            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print("Error al eliminar medicamento:", str(ex))
            return False