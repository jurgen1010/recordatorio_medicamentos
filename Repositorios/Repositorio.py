import pyodbc
from Entidades import Medicamento
from Utilidades.Configuracion import Configuracion

class MedicamentosRepositorio:

    def Listar(self) -> list:
        try:
            print("Cadena de conexión:", Configuracion.strConnection)  # Depuración
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