# importando sqlite
import sqlite3 as lite

# criando conexão com banco de dados
conexao = lite.connect('Oficina.db')

# criando tabela de clientes
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_clientes (id_client INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone INTEGER, nif INTEGER, morada TEXT)")

# inserindo dados na tabela de clientes
lista = ['Joao Futi Muanda', 'joao@mail.com', 933273210, 322613647, 'Praca Luis de Camoes N8']
with conexao:
     cur = conexao.cursor()
     query = "INSERT INTO tbl_clientes (nome, email, telefone, nif, morada) VALUES (?, ?, ?, ?, ?)"
     cur.execute(query, lista)

# acessando informações da tabela de clientes
with conexao:
    cur = conexao.cursor()
    query = "SELECT * FROM tbl_clientes"
    cur.execute(query)
    informacoes = cur.fetchall()
    print("Informações dos clientes:")
    for info in informacoes:
        print(info)

# atualizando informações na tabela de clientes
lista_atualizada = ['Lissandro Gay', 1]   
with conexao:
    cur = conexao.cursor()
    query = "UPDATE tbl_clientes SET nome = ? WHERE id_client = ?"
    cur.execute(query, lista_atualizada)
    
# eliminando informações na tabela de clientes
lista_atualizada = [1]   
with conexao:
    cur = conexao.cursor()
    query = "delete from  tbl_clientes  WHERE id_client = ?"
    cur.execute(query, lista_atualizada)    

    

    
    