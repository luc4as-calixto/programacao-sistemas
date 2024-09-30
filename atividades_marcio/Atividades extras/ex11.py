n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
soma = 0

if n1 < n2:
    for n1 in range(n1, n2 + 1):   
        print(n1)
        soma = soma + n1
else:
    for n1 in range(n1, n2 - 1, -1):
        print(n1)   
        soma = soma + n1

print("A soma dos números é: {}".format(soma))