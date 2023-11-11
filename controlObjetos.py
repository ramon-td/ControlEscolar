import mysql.connector as database
from mysql.connector import Error

class Usuarios:
    def __init__(self):
        try:
            self.conexion=database.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "",
                db = "proyecto"
            )
        except Error as ex:
            print("Error al intentar conexion")

    def listarUsuarios(self):
        
        if self.conexion.is_connected():
            try:
                listaUsuarios = [{}]
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios;")
                resultados = cursor.fetchall()
                for row in resultados:
                    self.idusuario = row[0]
                    self.nombre = row[1]
                    self.ap = row[2]
                    self.am = row[3]
                    self.usuario = row[4]
                    self.password = row[5]
                    self.perfil = row[6]
                    listaUsuarios.append({  "idusuario" : self.idusuario,
                                            "nombre" : self.nombre,
                                            "ap" : self.ap,
                                            "am" : self.am,
                                            "usuario" : self.usuario,
                                            "password" : self.password,
                                            "perfil" : self.perfil})
            except Error as ex:
                print("Error al intentar conexion")
        return listaUsuarios