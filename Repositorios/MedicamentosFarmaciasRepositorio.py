import pyodbc
from Entidades.MedicamentoFarmacia import MedicamentoFarmacia
from Utilidades import Configuracion

class MedicamentosFarmaciasRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "SELECT id, farmacia_id, medicamento_id, precio, stock FROM medicamentos_farmacias;"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                item = MedicamentoFarmacia(
                    id=elemento[0],
                    farmacia_id=elemento[1],
                    medicamento_id=elemento[2],
                    precio=float(elemento[3]),
                    stock=int(elemento[4])
                )
                lista.append(item)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar medicamentos_farmacias:", str(ex))
            return []

    def Guardar(self, medicamento_farmacia: MedicamentoFarmacia) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO medicamentos_farmacias (farmacia_id, medicamento_id, precio, stock)
                VALUES (?, ?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           medicamento_farmacia.farmacia_id,
                           medicamento_farmacia.medicamento_id,
                           medicamento_farmacia.precio,
                           medicamento_farmacia.stock)
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Registro guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el medicamento_farmacia:", str(ex))
            return "Error al guardar el registro"

    def Actualizar(self, medicamento_farmacia: MedicamentoFarmacia) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE medicamentos_farmacias
                SET farmacia_id = ?, medicamento_id = ?, precio = ?, stock = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta,
                           medicamento_farmacia.farmacia_id,
                           medicamento_farmacia.medicamento_id,
                           medicamento_farmacia.precio,
                           medicamento_farmacia.stock,
                           medicamento_farmacia.id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Registro con ID {medicamento_farmacia.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el registro:", str(ex))
            return "Error al actualizar el registro"

    def Eliminar(self, id: int) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = "DELETE FROM medicamentos_farmacias WHERE id = ?;"
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            conexion.commit()
            cursor.close()
            conexion.close()
            return f"Registro con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el registro:", str(ex))
            return "Error al eliminar el registro"
