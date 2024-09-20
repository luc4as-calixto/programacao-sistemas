base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for i in range(1, expoente + 1):
    resultado = base * resultado
print("O resultado de {} elevado a {} é: {}".format(base, expoente, resultado))