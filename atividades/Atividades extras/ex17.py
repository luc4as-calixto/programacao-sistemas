numero = int(input("Digite um número para ver o fatorial dele: "))

fatorial = numero

for i in range(1, numero):
    fatorial = fatorial * i

print("O fatorial do número {} é: {}".format(numero, fatorial))