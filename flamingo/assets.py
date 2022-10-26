import uuid
from datetime import datetime
from cryptography.fernet import Fernet
from flamingo.database.data_communication import database_select_one, database_update, database_insert

# módulo de funções que são pertinentes ao gerenciamento de assets.
# que funções queremos ter?
# 1 função de inserir novo assets (CREATE)
# 1 função para buscar os assets (READ)
# 1 função para atualizar os assets (UPDATE)
# 1 função para deletar os assets (DELETE)
# o módulo é um CRUD o/ yay~

# chave para criptografia e decrip..
key = b"7HGhFbNLtcS5QnEn69UbrrhMLIjBwUQ5DeBjvk56Ga0="
f = Fernet(key)

def menu_assets():
    print("Select the options:")
    print("1. Create assets\n")
    print("2. Read assets\n")
    print("3. Update assets\n")
    print("4. Delete assets\n")
    print("5. Exit\n")

    while True:
        choice = int(input("Select the number:"))

        if choice == 5:
            print("Bye bye")
            exit()

        if choice in (1, 2, 3, 4):
            return choice


# só nome e parâmetros (assinatura)
def create_assets(connection, user_name, password, url, name):
    token = f.encrypt(password.encode())
    database_insert(
        connection=connection,
        table_name="Assets",
        columns=["User_name", "Password", "URL", "Name", "ID", "Created_at"],
        values=[
            user_name,
            token.decode(),
            url,
            name,
            uuid.uuid4(),
            datetime.now().__str__(),
        ],
    )
    return True


def read_assets(connection, user_name):
    result = database_select_one(
        connection=connection,
        table_name="Assets",
        columns=["User_name", "Password", "URL", "Name"],
        condition=f"User_name = '{user_name}'",
    )
    user_name, password, url, name = result
    token = f.decrypt(password.encode())
    
    return user_name, token, url, name

    
def update_assets(connection, user_name, password, url, name):
    token = f.encrypt(password.encode())
    database_update(
        connection=connection,
        table_name="Assets",
        columns=["User_name", "Password", "URL", "Name", "Updated_at"],
        condition=f"User_name = '{user_name}'",
        values=[
            user_name,
            token.decode(),
            url,
            name,
            datetime.now().__str__(),
        ]
    )
    return True 


def delete_assets(connection, user_name):
    database_update(
        connection=connection,
        table_name="Assets",
        columns=["Deleted_at"],
        condition=f"User_name = '{user_name}'",
        values=[
            datetime.now().__str__(),
        ]
    )
    return True 
