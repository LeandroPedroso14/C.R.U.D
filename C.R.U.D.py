import mysql.connector

conexao = mysql.connector(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

cursor.close()
