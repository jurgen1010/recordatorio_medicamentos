import pyodbc
from Entidades import Medicamento;
from Utilidades import Configuracion;

class MedicamentosRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, nombre, dosis, duracion, usuario_id, categoria_id
                FROM medicamentos;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:

                medicamento = Medicamento.Medicamento(
                    id=elemento[0],
                    nombre=elemento[1],
                    dosis=elemento[2],
                    duracion=elemento[3],
                    usuario_id=elemento[4],
                    categoria_id=elemento[5]
                )
                lista.append(medicamento)

            cursor.close();
            conexion.close();
        
            return lista;
        except Exception as ex:
            print("Error al listar medicamentos:", str(ex))
            return []
        
    def Guardar(self, medicamento: Medicamento) -> str:
        try:
            # Conexión a la base de datos
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO medicamentos (nombre, dosis, duracion, usuario_id, categoria_id)
                VALUES (?, ?, ?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                        medicamento.nombre, 
                        medicamento.dosis, 
                        medicamento.duracion, 
                        medicamento.usuario_id, 
                        medicamento.categoria_id)
            
            # Obtener el ID del último registro insertado
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]

            # Confirmar los cambios
            conexion.commit()
            
            cursor.close()
            conexion.close()
            
            # Usar una f-string para retornar un mensaje con el ID insertado
            return f"Medicamento guardado exitosamente con ID: {id_insertado}"
        
        except Exception as ex:
            print("Error al guardar el medicamento:", str(ex))
            return "Error al guardar el medicamento"
        
    def Actualizar(self, medicamento: Medicamento) -> str:
        try:
            # Conexión a la base de datos
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE medicamentos
                SET nombre = ?, dosis = ?, duracion = ?, usuario_id = ?, categoria_id = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                        medicamento.nombre, 
                        medicamento.dosis, 
                        medicamento.duracion, 
                        medicamento.usuario_id, 
                        medicamento.categoria_id, 
                        medicamento.id)
            
            # Confirmar los cambios
            conexion.commit()
            
            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()
            
            return f"Medicamento con ID {medicamento.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el medicamento:", str(ex))
            return "Error al actualizar el medicamento"
        
    def Eliminar(self, id: int) -> str:
        try:
            # Conexión a la base de datos
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM medicamentos
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
            
            # Confirmar los cambios
            conexion.commit()
            
            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()
            
            return f"Medicamento con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el medicamento:", str(ex))
            return "Error al eliminar el medicamento"