import mysql.connector

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

# CRUD

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#conexao.commit() # Para editar banco de dados.
resultado = cursor.fetchall() # Ler o banco de dados.
print(resultado)


cursor.close()
conexao.close()

# CREATE
#nome_produto = "leite"
#valor = 4
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() # Para editar banco de dados.

# READ
