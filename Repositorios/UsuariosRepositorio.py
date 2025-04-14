import pyodbc
from Entidades.Usuario import Usuario
from Utilidades import Configuracion

class UsuariosRepositorio:

    def Listar(self) -> list:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT id, nombre, correo, contraseña
                FROM usuarios;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista: list = []
            for elemento in cursor:
                usuario = Usuario(
                    id=elemento[0],
                    nombre=elemento[1],
                    correo=elemento[2],
                    contraseña=elemento[3]
                )
                lista.append(usuario)

           
            cursor.close()
            conexion.close()

            return lista
        except Exception as ex:
            print("Error al listar usuarios:", str(ex))
            return []

    def Guardar(self, usuario: Usuario) -> str:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                INSERT INTO usuarios (nombre, correo, contraseña)
                VALUES (?, ?, ?);
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           usuario.nombre, 
                           usuario.correo, 
                           usuario.contraseña)
            
            # Obtener el ID del último registro insertado
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_insertado = cursor.fetchone()[0]

            # Confirmar los cambios
            conexion.commit()

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return f"Usuario guardado exitosamente con ID: {id_insertado}"
        except Exception as ex:
            print("Error al guardar el usuario:", str(ex))
            return "Error al guardar el usuario"

    def Actualizar(self, usuario: Usuario) -> str:
        try:
           
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                UPDATE usuarios
                SET nombre = ?, correo = ?, contraseña = ?
                WHERE id = ? AND NOT EXISTS (
                    SELECT 1 FROM usuarios WHERE correo = ? AND id != ?
                );
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, 
                           usuario.nombre, 
                           usuario.correo, 
                           usuario.contraseña, 
                           usuario.id,
                           usuario.correo,  # Verificar si el correo ya existe en otro usuario
                           usuario.id)
            
            # Confirmar los cambios
            if cursor.rowcount == 0:
                raise Exception("El correo ya está en uso por otro usuario.")


            conexion.commit()

            cursor.close()
            conexion.close()

            return f"Usuario con ID {usuario.id} actualizado exitosamente"
        except Exception as ex:
            print("Error al actualizar el usuario:", str(ex))
            return "Error al actualizar el usuario"

    def Eliminar(self, id: int) -> str:
        try:            
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                DELETE FROM usuarios
                WHERE id = ?;
            """
            cursor = conexion.cursor()
            cursor.execute(consulta, id)
                    
            conexion.commit()
            
            cursor.close()
            conexion.close()

            return f"Usuario con ID {id} eliminado exitosamente"
        except Exception as ex:
            print("Error al eliminar el usuario:", str(ex))
            return "Error al eliminar el usuario"