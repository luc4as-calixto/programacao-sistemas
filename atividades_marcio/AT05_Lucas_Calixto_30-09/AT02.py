lista1 = []
lista2 = []

for i in range(5):
    numero1 = int(input(f"Digite o {i + 1}º número para a lista 1: "))
    lista1.append(numero1)
    numero2 = int(input(f"Digite o {i + 1}º número para a lista 2: "))
    lista2.append(numero2)

quant = 0

for i in range(5):

    for j in range(5):

        if lista1[i] == lista2[j]:
            quant = quant + 1
            print(lista1[i])

if quant == 0:
    print("Não tem")