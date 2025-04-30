import mysql.connector



# Conectar ao banco de dados MySQL
def conectar():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Seu usuário MySQL
        password="",  # Sua senha MySQL
        database="cadastro_pessoas"
    )
    return conn


# Função para cadastrar pessoa
def cadastrar(nome, idade, email):
    conn = conectar()
    cursor = conn.cursor()

    query = "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, idade, email))

    conn.commit()
    print(f"Pessoa {nome} cadastrada com sucesso!")
    cursor.close()
    conn.close()


# Função para listar todas as pessoas cadastradas
def listar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()

    for pessoa in pessoas:
        print(f"ID: {pessoa[0]} | Nome: {pessoa[1]} | Idade: {pessoa[2]} | Email: {pessoa[3]}")

    cursor.close()
    conn.close()


# Função para editar uma pessoa
def editar(id, nome, idade, email):
    conn = conectar()
    cursor = conn.cursor()

    query = "UPDATE pessoas SET nome=%s, idade=%s, email=%s WHERE id=%s"
    cursor.execute(query, (nome, idade, email, id))

    conn.commit()
    print(f"Pessoa com ID {id} editada com sucesso!")
    cursor.close()
    conn.close()


# Função para excluir uma pessoa
def excluir(id):
    conn = conectar()
    cursor = conn.cursor()

    query = "DELETE FROM pessoas WHERE id=%s"
    cursor.execute(query, (id,))

    conn.commit()
    print(f"Pessoa com ID {id} excluída com sucesso!")
    cursor.close()
    conn.close()


# Menu de opções
def menu():
    while True:
        print("\nSistema de Cadastro")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Editar pessoa")
        print("4. Excluir pessoa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            email = input("Email: ")
            cadastrar(nome, idade, email)
        elif opcao == "2":
            listar()
        elif opcao == "3":
            id = int(input("ID da pessoa que deseja editar: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            editar(id, nome, idade, email)
        elif opcao == "4":
            id = int(input("ID da pessoa que deseja excluir: "))
            excluir(id)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Rodar o menu
if __name__ == "__main__":
    menu()
