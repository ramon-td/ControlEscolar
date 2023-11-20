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
            print("Error al intentar conexion: " + ex)
    
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
                
                for row in resultados:
                    for x in range(len(row)):
                        if row[x] is None:
                            data.append("")
                        else:
                            data.append(row[x])

                for row in QueryInfo:
                    key.append(row[0])

                for x in range(len(data)):
                    Objeto.setdefault(key[x], data[x])

                # print(Objeto.items())

            except Error as ex:
                print("Error al intentar conexion" + str(ex))
        return Objeto
    
    def actualizarObjeto(self, objeto, id):
        sentence = ""
        for key in objeto.items():
            sentence += key[0] + " = \"" + key[1] + "\","
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE usuarios SET " + sentence[:-1] +  " WHERE idusuario = " + str(id) + ";")
        self.conexion.commit()
        


