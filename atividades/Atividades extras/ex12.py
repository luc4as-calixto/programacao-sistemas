numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print("{} x {} = {}".format(numero, i, numero * i))