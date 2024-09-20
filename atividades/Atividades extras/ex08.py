soma = 0
for i in range(1, 6):
    n = int(input("Digite o {}º número: ".format(i)))
    soma = n + soma
media = soma / 5
print("A média dos números é: {}".format(media))