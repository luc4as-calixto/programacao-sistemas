#Exercicio pedra,papel e tesoura, versão 3

#importa o modulo randint de random
from random import randint

def jogo():

    jogador1 = int(input("Digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
    jogador2 = randint(0, 2)

    print("")
    print("Jogador 1 escolheu ", jogador1)
    print("Jogador 2 escolheu ", jogador2, "\n")

    #olha para ver se o usuário digitou as opções corretas
    if jogador1 >= 0 and jogador1 <= 2:

        #olha quem ganhou ou se deu empate
        if jogador1 == jogador2:
            print("Empate")
        elif (jogador1 == 0) and (jogador2 == 2) or (jogador1 == 1) and (jogador2 == 0) or (jogador1 == 2) and (jogador2 == 1):
            print("Jogador 1 ganhou")
        elif (jogador2 == 0) and (jogador1 == 2) or (jogador2 == 1) and (jogador1 == 0) or (jogador2 == 2) and (jogador1 == 1):
            print("Jogador 2 ganhou")

        print("")
        continuar = input("Deseja continuar? (S/N)")
        print("")

        #confira se o usuário deseja continuar
        if continuar == "S" or continuar == "s":
            jogo()

    else:
        print("Opção inválida")
        continuar = input("Deseja continuar? (S/N)")
        if continuar == "S" or continuar == "s":
            jogo()

#inicio, chama a função jogo
jogo()