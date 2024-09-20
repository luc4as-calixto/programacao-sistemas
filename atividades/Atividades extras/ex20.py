def calcular_fatorial():
    numero = int(input("Digite um número para ver o fatorial dele: "))

    if numero > 0 and numero <= 16:

        fatorial = numero

        for i in range(1, numero):
            fatorial = fatorial * i

        print("O fatorial do número {} é: {}".format(numero, fatorial))

        pergunta = str(input("Deseja ver o fatorial de outro número? (s/n) "))

        if "s" in pergunta or "S" in pergunta:
            calcular_fatorial()
        else:
            print("Fim do programa.")
    
    else:
        print("Digite um número entre 0 e 16.")
        calcular_fatorial()

calcular_fatorial()