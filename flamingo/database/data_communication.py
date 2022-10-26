# interfaces de comunicação com banco de dados.

import sqlite3

DATABASE_NAME = "Flamingo.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


# VÁRIAS FUNÇÕES


def database_insert(connection, table_name, columns, values):
    # INSERT INTO 'nome da tabela' (colunas*) values ('',''), ('','');
    command = "INSERT INTO {table_name} ({columns}) values ({values});"  # sql com variáveis de substituição
    data = command.format(
        table_name=table_name,
        columns=",".join(columns),
        values=",".join(f"'{v}'" for v in values),
    )
    cur = connection.cursor()
    cur.execute(data)
    connection.commit()  # con = connection


def database_select(connection, table_name, columns, condition):
    # retorna todos os registros do banco com base em uma condição
    # SELECT * FROM Funcionario WHERE Nome
    command = "SELECT {columns} FROM {table_name} WHERE {condition}"
    data = command.format(
        table_name=table_name, columns=",".join(columns), condition=condition
    )
    cur = connection.cursor()
    response = cur.execute(data)
    return response.fetchall()


def database_select_one(connection, table_name, columns, condition):
    # retorna um registro do banco com base em uma condição
    # SELECT * FROM Funcionario WHERE Nome
    command = "SELECT {columns} FROM {table_name} WHERE {condition}"
    data = command.format(
        table_name=table_name, columns=",".join(columns), condition=condition
    )
    cur = connection.cursor()
    response = cur.execute(data)
    return response.fetchone()


def database_update(connection, table_name, columns, values, condition):
    # retorna um registro do banco com base em uma condição
    # UPDATE table_name SET column1 = value1 WHERE condition;
    command = "UPDATE {table_name} SET {columns} WHERE {condition}"
    columns_with_values = []
    for key, value in zip(columns, values): #loop que unifica duas listas e transforma em uma lista de tuplas (coluna(chave) e valor).
        columns_with_values.append(f"{key}='{value}'") #adc valor na lista vazia (string formatada com chaves e valores)
    
    data = command.format(
        table_name=table_name, columns=",".join(columns_with_values), condition=condition #formatação com base nos placeholders
    )
    cur = connection.cursor()
    cur.execute(data)
    connection.commit() 