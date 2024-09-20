def pergunta(quantidade):
    maior = 0
    menor = 1001  # inicializa o menor com um valor maior que o máximo permitido
    posicaomaior = 0
    posicaomenor = 0
    soma = 0

    for i in range(1, quantidade + 1):
        numero = float(input("Digite o {}º número: ".format(i)))
        if numero >= 0 and numero <= 1000:
            if numero > maior:
                maior = numero
                posicaomaior = i
            if numero < menor:
                menor = numero
                posicaomenor = i

            soma += numero
        else:
            print("Digite um número entre 0 e 1000.")
            return pergunta(quantidade)

    print("O maior número é {} e foi o {}º a ser digitado.".format(maior, posicaomaior))
    print("O menor número é {} e foi o {}º a ser digitado.".format(menor, posicaomenor))
    print("A soma dos números é: {}".format(soma))

quantidade = int(input("Digite a quantidade de números: "))

pergunta(quantidade)