from contextlib import closing

# FUNÇÕES AUXILIARES DO BANCO DE DADOS.

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

# BANCO DE DADOS DAQUI PRA BAIXO.

def conectar():
    import sqlite3
    return sqlite3.connect("cliente.db")

def sql_create():
    with open("create.sql", "r") as f:
        return f.read()

def criar_bd():
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.executescript(sql_create())
        con.commit()

def buscar_cliente(id_cliente):
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute("SELECT * FROM cliente WHERE id_cliente = ?", [id_cliente])
        return row_to_dict(cursor.description, cursor.fetchone())

def listar_clientes():
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute("SELECT * FROM cliente")
        return rows_to_dict(cursor.description, cursor.fetchall())

def inserir_cliente(nome, comentario):
    sql = "INSERT INTO cliente (nome, comentario) VALUES (?, ?)"
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute(sql, [nome, comentario])
        id_cliente = cursor.lastrowid
        con.commit()
    return id_cliente

def alterar_cliente(id_cliente, nome, comentario):
    sql = "UPDATE cliente SET nome = ?, comentario = ? WHERE id_cliente = ?"
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute(sql, [nome, comentario, id_cliente])
        con.commit()

def deletar_cliente(id_cliente):
    sql = "DELETE FROM cliente WHERE id_cliente = ?"
    with closing(conectar()) as con, closing(con.cursor()) as cursor:
        cursor.execute(sql, [id_cliente])
        con.commit()

# FRONT-END TOSCO COM INPUT E PRINT DAQUI PRA BAIXO.

def pedir_inserir_cliente():
    nome = input("Digite o nome do novo cliente: ")
    comentario = input("Digite o comentário acerca dele(a): ")
    id_cliente = inserir_cliente(nome, comentario)
    print(f"O(a) cliente com o id {id_cliente} foi criado(a).")

def pedir_alterar_cliente():
    id_cliente_str = input("Digite o id de um cliente já existente: ")
    try:
        id_cliente = int(id_cliente_str)
    except:
        print("Era pra você digitar um número!")
        return
    if buscar_cliente(id_cliente) is None:
        print("Esse cliente não existe!")
        return
    nome = input("Digite o novo nome do novo cliente: ")
    comentario = input("Digite o novo comentário acerca dele(a): ")
    alterar_cliente(id_cliente, nome, comentario)
    print(f"O(a) cliente com o id {id_cliente} foi alterado(a).")

def pedir_excluir_cliente():
    id_cliente_str = input("Digite o id de um cliente já existente: ")
    try:
        id_cliente = int(id_cliente_str)
    except:
        print("Era pra você digitar um número!")
        return
    if buscar_cliente(id_cliente) is None:
        print("Esse cliente não existe!")
        return
    deletar_cliente(id_cliente)
    print(f"O(a) cliente com o id {id_cliente} foi deletado(a).")

def mostrar_cliente(cliente):
    print("Valores:")
    for campo in cliente:
        print(f"    {campo}: {cliente[campo]}")

def listar_todos_clientes():
    lista = listar_clientes()
    for cliente in lista:
        mostrar_cliente(cliente)

def pedir_mostrar_cliente():
    id_cliente_str = input("Digite o id de um cliente já existente: ")
    try:
        id_cliente = int(id_cliente_str)
    except:
        print("Era pra você digitar um número!")
        return
    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        print("Esse cliente não existe!")
        return
    mostrar_cliente(cliente)

def menu():
    escolha = ""
    while escolha != "6":
        print("")
        print("Escolha 1 para buscar cliente.")
        print("Escolha 2 para listar todos os clientes.")
        print("Escolha 3 para cadastrar cliente.")
        print("Escolha 4 para alterar cliente.")
        print("Escolha 5 para deletar cliente.")
        print("Escolha 6 para sair.")

        escolha = input("Sua escolha: ")

        if escolha == "1":
            pedir_mostrar_cliente()
        elif escolha == "2":
            listar_todos_clientes()
        elif escolha == "3":
            pedir_inserir_cliente()
        elif escolha == "4":
            pedir_alterar_cliente()
        elif escolha == "5":
            pedir_excluir_cliente()
        elif escolha == "6":
            print("Tchau.")
        else:
            print("Não entendi. Vamos tentar de novo.")

criar_bd()
menu()