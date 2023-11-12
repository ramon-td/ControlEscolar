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
                    failsafe = []
                    for x in range(0, 7):
                        if row[x] is None:
                            failsafe.append("")
                        else:
                            failsafe.append(row[x])

                    self.idusuario = failsafe[0]
                    self.nombre = failsafe[1]
                    self.ap = failsafe[2]
                    self.am = failsafe[3]
                    self.usuario = failsafe[4]
                    self.password = failsafe[5]
                    self.perfil = failsafe[6]
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