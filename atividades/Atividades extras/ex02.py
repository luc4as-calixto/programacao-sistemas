def login():

    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if nome == senha:
        print("")
        print("Senha igual ao nome")
        print("Digite novamente as informações")
        login()

login()