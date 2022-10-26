# módulo que controla o workflow de autenticação
# uma função de login (acesso) e uma função de criar usuário
import hashlib
from flamingo.database.data_communication import database_insert, database_select_one
from datetime import datetime
import uuid


def create_user(connection, email, password):
    result = database_select_one(
        connection, "Autenticacao", columns=["Email"], condition=f"Email = '{email}'"
    )
    if result:  # () -> False, (blablah,) -> True
        print("Email already exists.")
        return False

    secure_password = hashlib.sha256(
        password.encode()
    ).hexdigest()  # cifragem = texto para texto cifrado
    database_insert(
        connection,
        "Autenticacao",
        columns=["Email", "Senha", "ID", "Created_at"],
        values=[email, secure_password, uuid.uuid4(), datetime.now().__str__()],
    )
    return True


def login(connection, email, password):
    # 1ª verificação (se existem resultados)
    # 2ª verificação (se os emails são iguais)
    # 3ª verificação (se as senhas são iguais)

    # retorna uma tupla (email, senha) ou ()
    result = database_select_one(
        connection,
        "Autenticacao",
        columns=["Email", "Senha"],
        condition=f"Email = '{email}'",
    )

    # caso não retorne nenhum registro do banco, faça um print e termine a função
    if not result:  # () -> True, (blablah,) -> False
        print("Email not found.")
        return False

    # email      password         (email, password) <- tupla
    local_email, local_password = result  # tuplas que vem do banco de dados (local_*)

    check_password = hashlib.sha256(password.encode()).hexdigest()
    if check_password != local_password:
        print("Password mismatch.")
        return False

    return True
