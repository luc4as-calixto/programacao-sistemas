def maior_menor(lista):
    #a lista onde sera colocado os número
    maior = lista[0]
    menor = lista[0]
    #vai ver qual é o maior número
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        #vai ver qual é o menor número
        elif elemento < menor:
            menor = elemento
    #retorna os resultados
    return maior, menor

#inicializa uma lista
lista=list()
i=1
#faz as 10 perguntas para o usuário e coloca no lista e escreve ela
while i<=10:
    elem = int(input("Digite um elemento da lista:"))
    lista.append(elem)
    i+=1
    print(lista)
    #separa o maior e o menor número
maior, menor = maior_menor(lista)
#chama a função
print("Maior:", maior)
print("Menor:", menor)
