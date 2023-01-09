import mysql.connector

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

cursor.close()
conexao.close()
