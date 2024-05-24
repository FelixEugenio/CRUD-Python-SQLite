# importando SQLite
import sqlite3 as lite

# criando conexao com banco de dados
conexao = lite.connect('Oficina.db')

#criando as tabelas

with conexao:
    cur = conexao.cursor()
    cur.execute("create table tbl_clientes(id_client integer primary key autoincrement,nome text, email text,telefone integer,nif integer , morada text)")
