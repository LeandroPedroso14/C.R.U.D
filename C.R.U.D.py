import mysql.connector

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

# CRUD
nome_produto = "café"
valor = 5
comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (nome, valor)'
cursor.execute(comando)
conexao.commit() # Para editar banco de dados.
resultado = cursor.fetchall() # Ler o banco de dados.



cursor.close()
conexao.close()
