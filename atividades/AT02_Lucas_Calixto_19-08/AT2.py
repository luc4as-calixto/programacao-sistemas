#Exercicio pedra,papel e tesoura, versão 1

from random import randint
jogador1 = int(input("Digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
jogador2 = randint(0, 2)

print("")
print("Jogador 1 escolheu ", jogador1)
print("Jogador 2 escolheu ", jogador2, "\n")

if jogador1 == jogador2:
    print("Empate")
elif (jogador1 == 0) and (jogador2 == 2) or (jogador1 == 1) and (jogador2 == 0) or (jogador1 == 2) and (jogador2 == 1):
    print("Jogador 1 ganhou")
elif (jogador2 == 0) and (jogador1 == 2) or (jogador2 == 1) and (jogador1 == 0) or (jogador2 == 2) and (jogador1 == 1):
    print("Jogador 2 ganhou")