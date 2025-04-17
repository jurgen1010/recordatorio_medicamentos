import pyodbc
from Entidades.Categoria import Categoria
from Utilidades import Configuracion

class CategoriasRepositorio:

    def Listar(self) -> list:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, nombre
                FROM categorias;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:                
                categoria = Categoria(
                    id=elemento[0],
                    nombre=elemento[1]
                )
                lista.append(categoria)

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return lista
        except Exception as ex:
            print("Error al listar categorías:", str(ex))
            return []

    def Guardar(self, categoria: Categoria) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO categorias (nombre)
                VALUES (?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, categoria.nombre)
                        
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]

            # Confirmar los cambios
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Categoría guardada exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar la categoría:", str(ex))
            return "Error al guardar la categoría"

    def Actualizar(self, categoria: Categoria) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE categorias
                SET nombre = ?
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, categoria.nombre, categoria.id)
                        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Categoría con ID {categoria.id} actualizada exitosamente"
        except Exception as ex:
            print("Error al actualizar la categoría:", str(ex))
            return "Error al actualizar la categoría"

    def Eliminar(self, id: int) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM categorias
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
                        
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Categoría con ID {id} eliminada exitosamente"
        except Exception as ex:
            print("Error al eliminar la categoría:", str(ex))
            return "Error al eliminar la categoría"