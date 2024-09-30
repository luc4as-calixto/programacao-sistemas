def potencia():

    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    resultado = 1

    for i in range(expoente):
        resultado = base * resultado

    print(f"A potência de {base} elevado a {expoente} é {resultado}.")

potencia()