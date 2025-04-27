import mysql.connector

class Articulos:
    def abrir(self):
        conexion = mysql.connector.connect (host="locarlhost", user="root", password="", database="bd2")
        return conexion
   
    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos (descripcion, precios) values(%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def conculta(self, datos)
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos "where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall() #Devuelve a la Lista de TUPLAS
    
    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos" from articulos where codigo=%s"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall() #Devuelve a la Lista de TUPLAS