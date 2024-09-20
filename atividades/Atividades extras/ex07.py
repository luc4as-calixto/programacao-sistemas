maior = 0
for i in range(1, 6):
    n = int(input("Digite o {}º número: ".format(i)))
    if(n > maior):
        maior = n
        numero = i
print("O maior número é {} que foi o {}º a ser digitado".format(maior, numero))