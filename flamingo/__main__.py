# arquivo e função main servem para definir fluxo de execução.
# controla ciclo de vida do programa
# import flamingo.database.data_communication
from getpass import getpass
from secrets import choice
from flamingo.database.data_communication import create_connection
from flamingo.database.migrations import create_tables
from flamingo.authentication import create_user, login
from getpass import getpass
from flamingo.assets import create_assets, delete_assets, menu_assets, read_assets, update_assets


def menu():
    print("Welcome to Flamingo\n")
    print("Select the options:")
    print("1. Login\n")
    print("2. Create account\n")
    print("3. Exit\n")

    while True:
        choice = int(input("Select the number:"))

        if choice == 3:
            print("Bye bye")
            exit()

        
        # verificando se a opção do usuário está entre 1 e 2
        #                 () <- tuplas (compara o valor)
        #                 [] <- listas (compara o valor)
        #                 {} <- dicionários (somente a chave, não o valor)
        if choice in (1, 2):
            return choice
    

def main():
    # connection é uma só e é repassada para todas as funções
    connection = create_connection() # criando uma nova conexão com sqlite
    create_tables(connection) # criando tabelas, utilizando conexão com sqlite, préviamente criada.

    user_choice = menu()

    user_email = input("What's your email? \n")
    user_password = getpass("What's your password? \n") # senha não vai aparecer no terminal
    
    if user_choice == 2:
        is_user_created = create_user(connection, user_email, user_password)
        if is_user_created: # Retornou True
            print("User registered.")
        else:
            print("User already exists.")
        exit()

    if user_choice == 1:
        is_user_logged = login(connection, user_email, user_password)
        if is_user_logged:
            print("User authenticated.\n")
            assets_choice = menu_assets()
            if assets_choice == 1:
                user_name = input("What's your user name?\n")
                password = input("What's your password?\n")
                url = input("What's the url?\n")
                name = input("What's the name?\n")
                create_assets(connection, user_name=user_name, password=password, url=url, name=name)
                print("\nAssets created successfully!\n")

            if assets_choice == 2:
                user_name = input("What's your user name?\n")
                user_name, password, url, name = read_assets(connection, user_name=user_name)
                print("Your assets are:\n User Name: {} | Password: {} | URL: {} | Name: {}".format(user_name, password, url, name))

            if assets_choice == 3:
                user_name = input("What's your user name?\n")
                password = input("What's your password?\n")
                url = input("What's the url?\n")
                name = input("What's the name?\n")
                update_assets(connection, user_name=user_name, password=password, url=url, name=name)
                print("\nAssets updated successfully!\n")
            
            if assets_choice == 4:
                user_name = input("What's your user name?\n")
                delete_assets(connection, user_name=user_name)
                print("\nAssets deleted successfully!\n")

        else:
            print("User not authenticated.")


if __name__ == "__main__":
    main()


# 1º conectar ao banco +
# 2º criar as tabelas do banco (2) = login e senhas +
# 3º executar os comandos de sql +
 
# cadastro de senhas (assets)
 # montar tabela +
 # montar módulo
 # incluir esse módulo, a partir do login (se usuário logado -> cadastro de senha)
 