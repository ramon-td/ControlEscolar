import mysql.connector as database
from mysql.connector import Error

class Conexion:
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
            print("Error al intentar conexion: " + str(ex))
    
    def usuarioActivo(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("UPDATE usuarios SET estatus = 0;")
                self.conexion.commit()
                cursor.execute("UPDATE usuarios SET estatus = 1 WHERE idusuario = \"" + str(id) + "\";")
                self.conexion.commit()
                return 0
            except Error as ex:
                print("Error al intentar conexion" + str(ex))
                return 1
    def obtenerTablaCompleta(self, tabla):
        if self.conexion.is_connected():
            try:
                listaObjetos = []
                Objeto = {}
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM " + tabla + ";")
                resultados = cursor.fetchall()
                cursor.execute("SHOW COLUMNS FROM " + tabla + ";")
                QueryInfo = cursor.fetchall()

                data = []
                key = []
                
                if resultados:
                    for row in resultados:
                        for x in range(len(row)):
                            if row[x] is None:
                                data.append("")
                            else:
                                data.append(row[x])
                        for row in QueryInfo:
                            key.append(row[0])

                        for x in range(len(key)):
                            Objeto.setdefault(key[x], data[x])
                        listaObjetos.append(Objeto)
                        Objeto = {}
                        data = []
                        key = []

            except Error as ex:
                print("Error al intentar conexion" + str(ex))
        return listaObjetos

    def obtenerColumna(self, tabla, columna):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT " + columna + " FROM " + tabla + ";")
                resultados = cursor.fetchall()
                
                listaColumna = ()
                for campo in resultados:
                    if str(campo)[1] == "\'":
                        listaColumna += str(campo)[2:-3],
                    else:
                        listaColumna += str(campo)[1:-2],

                return listaColumna
            
            except Error as ex:
                print("Error al intentar conexion" + str(ex))

    def obtenerColumnaEspecifica(self, tabla, columna, fila, que):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT " + columna + " FROM " + tabla + " WHERE " + fila + " = " + str(que) )
                # cursor.execute("SELECT idusuario FROM usuarios WHERE estatus = 1")
                resultados = cursor.fetchone()
                # for campo in resultados: 
                #     print(campo)
                # print("SELECT " + columna + " FROM " + tabla + " WHERE " + fila + " = \"" + que + "\";")
                print(resultados)
                return resultados
            
            except Error as ex:
                print("Error al intentar conexion" + str(ex))

    def obtenerObjeto(self, tabla, columna, que):
        if self.conexion.is_connected():
            try:
                Objeto = {}
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM " + tabla + " WHERE " + columna +  " = \"" + que + "\";")
                resultados = cursor.fetchall()
                cursor.execute("SHOW COLUMNS FROM " + tabla + ";")
                QueryInfo = cursor.fetchall()

                data = []
                key = []
                
                if resultados:
                    for row in resultados:
                        for x in range(len(row)):
                            if row[x] is None:
                                data.append("")
                            else:
                                data.append(row[x])
                        # print(str(row))

                    for row in QueryInfo:
                        key.append(row[0])
                        # print(str(row))

                    for x in range(len(key)):
                        Objeto.setdefault(key[x], data[x])

                # print(Objeto.items())

            except Error as ex:
                print("Error al intentar conexion" + str(ex))
        return Objeto
  
    def actualizarObjeto(self, objeto, tabla, columna, fila):
         if self.conexion.is_connected():
            try:
                sentence = ""
                for key in objeto.items():
                    sentence += str(key[0]) + " = \"" + str(key[1]) + "\","
                cursor = self.conexion.cursor()
                cursor.execute("UPDATE " + tabla + " SET " + sentence[:-1] +  " WHERE " + columna + " = \"" + str(fila) + "\";")
                self.conexion.commit()
                return 0
            except Error as ex:
                print("Error al intentar conexion" + str(ex))
                return 1

    def insertarNuevoObjeto(self, objeto, tabla):
         if self.conexion.is_connected():
            try:
                keys = ""
                values = ""

                for key in objeto.keys():
                    keys += key + ","
                for value in objeto.values():
                    values += "\"" + str(value) + "\","
                # print("INSERT INTO " + tabla + " (" + keys[:-1] +  ") VALUES (" + values[:-1] + ");")
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO " + tabla + " (" + keys[:-1] +  ") VALUES (" + values[:-1] + ");")
                self.conexion.commit()
                return 0
            except Error as ex:
                print("Error al intentar inserción: " + str(ex))
                return 1

    def eliminarObjeto(self, tabla, id, columna):
        if self.conexion.is_connected():
            try:
                # print("INSERT INTO " + tabla + " (" + keys[:-1] +  ") VALUES (" + values[:-1] + ");")
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM " + tabla + " WHERE " +columna +  " = \"" + id + "\";")
                self.conexion.commit()
                return 0
            except Error as ex:
                print("Error al intentar eliminar el objeto: " + str(ex))
                return 1