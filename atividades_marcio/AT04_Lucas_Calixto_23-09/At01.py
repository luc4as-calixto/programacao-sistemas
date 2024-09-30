def reverte():

    numero = int(input("Digite um número inteiro: "))

    numero = str(numero)
    for i in range(len(numero)-1, -1, -1):
        print(numero[i], end="")

reverte()