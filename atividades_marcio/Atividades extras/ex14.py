quantpar = 0
quantimpar = 0
numeros = []

for i in range(1, 11):
    numero = int(input("Digite o {}º número: ".format(i)))
    numeros.append(numero)

print("")

for numero in numeros:
    if numero % 2 == 0:
        quantpar += 1
        print("O número {} é par".format(numero))
    else:
        quantimpar += 1
        print("O número {} é ímpar".format(numero))

print("")
print("A quantidade de números pares é {}".format(quantpar))
print("A quantidade de números ímapares é {}".format(quantimpar))