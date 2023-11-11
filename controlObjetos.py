import mysql.connector as database
from mysql.connector import Error
#Test

class Usuarios:
    def __init__(self):
        #Conexion a bdd para sacar los objetos necesarios
        
        try:
            self.conexion=database.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                db="proyecto"
            )
        except Error as ex:
            print("Error al intentar conexion")
        
        self.usuario1 = "Admin"
        self.contra1 = "AdminP"
        self.usuario2 = "Maestro"
        self.contra2 = "MaestroP"
        self.usuario3 = "Alumno"
        self.contra3 = "AlumnoP"
        #self.privilegios = 1
        # for x in range(0, 4):

    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios;")
                resultados=cursor.fetchall()
                contador =1
                for row in resultados:
                    print("ID: {0}. Nombre: '{1}'".format(contador, row[1], row[2]))
                    contador = contador +1
                return resultados
            except Error as ex:
                print("Error al intentar conexion")
                
        
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