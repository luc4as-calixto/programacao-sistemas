numeros = []
#faz as perguntas1
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!!!")
#faz a soma
soma = sum(numeros)
#faz a media
media = soma / len(numeros)
#escreve a some e a media
print("Soma:", soma)
print("Média:", media)