# operações com tabelas

# definição das tabelas
# criação das tabelas = desenhar
# executar tabelas

# chave é o nome representativo, valor é o sql da tabela.


# Aqui são definidas as tabelas
MIGRATION_TABLES = {
    # identificador : tabela em si (valor)
    "login": """
CREATE TABLE IF NOT EXISTS Autenticacao(
    Email VARCHAR(100), 
    Senha VARCHAR(100),
    ID VARCHAR,
    Created_at TIMESTAMP,
    Deleted_at TIMESTAMP,
    Updated_at TIMESTAMP
);  

    """,  # aspas triplas = strings, linhas longas
    "assets": """ 
    CREATE TABLE IF NOT EXISTS Assets(
    User_name VARCHAR(100),
    Password VARCHAR(200),
    URL VARCHAR(100),
    Name VARCHAR(100),
    ID VARCHAR,
    Created_at TIMESTAMP,
    Deleted_at TIMESTAMP,
    Updated_at TIMESTAMP
);  
    """,
}


def create_tables(connection):
    cur = connection.cursor()  # *possibilita* executar um comando.
    for key, value in MIGRATION_TABLES.items():
        cur.execute(value)


# para cada item do dicionário, vai executar o valor (criar tabela).
