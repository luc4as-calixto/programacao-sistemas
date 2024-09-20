quantidade = int(input("Digite a quantidade de números: "))
maior = 0 
posicao = 0
soma = 0 
numero = int(input("Digite o 1º número: "))
menor = numero
posicaomenor = 1
for i in range(2, quantidade + 1):
    numero = int(input("Digite o {}º número: ".format(i)))
    if numero > maior:
        maior = numero
        posicaomaior = i
    elif numero < menor:
        menor = numero
        posicaomenor = i
    
    soma = soma + numero 
    
print("O maior número é {} que foi o {}º a ser digitado".format(maior, posicaomaior))
print("O menor número é {} que foi o {}º a ser digitado".format(menor, posicaomenor))
print("A soma dos números é: {}".format(soma))