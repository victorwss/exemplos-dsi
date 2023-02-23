from contextlib import closing

sql_create = """
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    comentario TEXT,
    genero TEXT
) STRICT;

INSERT INTO cliente(nome, comentario, genero) VALUES ('Zé', 'Primeiro cliente', 'M');
INSERT INTO cliente(nome, comentario, genero) VALUES ('Maria', 'cliente 2', 'F');
"""

# Converte uma linha em um dicionário.
def row_to_dict(description, row):
    if row is None: return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d

# Converte uma lista de linhas em um lista de dicionários.
def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result

def conectar():
    import sqlite3
    return sqlite3.connect("cliente.db")

def criar_bd():
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.executescript(sql_create)
        con.commit()

def mostra_todos_tupla():
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute("SELECT id_cliente, nome, comentario FROM cliente")
        rows = cursor.fetchall()
        for (id_cliente, nome, comentario) in rows:
            print("valores:", id_cliente, nome, comentario)

def mostra_todos_dicionario():
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute("SELECT * FROM cliente")
        dicionarios = rows_to_dict(cursor.description, cursor.fetchall())
        for registro in dicionarios:
            print("Valores:")
            for campo in registro:
                print(f"    {campo}: {registro[campo]}")

def inserir_cliente(nome, comentario, genero):
    sql = "INSERT INTO cliente (nome, comentario, genero) VALUES (?, ?, ?)"
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute(sql, (nome, comentario, genero))
        id_cliente = cursor.lastrowid
        con.commit()
    return id_cliente

def inserir_cliente_ruim(nome, comentario, genero):
    sql = f"INSERT INTO cliente (nome, comentario, genero) VALUES ('{nome}', '{comentario}', '{genero}')"
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.executescript(sql)
        id_cliente = cursor.lastrowid
        con.commit()
    return id_cliente

def pedir_dados_cliente():
    nome = input("Digite o nome do novo cliente: ")
    comentario = input("Digite o comentário acerca dele(a): ")
    genero = input("É M ou F? ")
    #id_cliente = inserir_cliente(nome, comentario, genero)
    id_cliente = inserir_cliente_ruim(nome, comentario, genero)
    print(f"O(a) cliente com o id {id_cliente} foi criado(a).")

#criar_bd()
pedir_dados_cliente()
mostra_todos_dicionario()