import mysql.connector

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

# CRUD
comando = ''
cursor.execute(comando)



cursor.close()
conexao.close()
