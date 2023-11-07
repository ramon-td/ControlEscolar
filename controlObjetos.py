import mysql.connector

class Usuarios:
    def __init__(self):
        #Conexion a bdd para sacar los objetos necesarios
        self.usuario1 = "Admin"
        self.contra1 = "AdminP"
        self.usuario2 = "Maestro"
        self.contra2 = "MaestroP"
        self.usuario3 = "Alumno"
        self.contra3 = "AlumnoP"
        #self.privilegios = 1
        # for x in range(0, 4):

    def listarUsuarios(self):
        listaUsuarios = [{}]
        listaUsuarios.append({"Username" : self.usuario1,
                              "Password" : self.contra1,
                              "Permisos" : 4})
        listaUsuarios.append({"Username" : self.usuario2,
                              "Password" : self.contra2,
                              "Permisos" : 3})
        listaUsuarios.append({"Username" : self.usuario3,
                              "Password" : self.contra3,
                              "Permisos" : 2})
        return listaUsuarios