def insertion_sort(lista):
    #modifica a lista para a ordem crescente
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1 
            lista[j + 1] = chave

#cria uma lista
lista=list()
i=1
#faz as 10 perguntas para o usuáiro e coloca na lista
while i<=10:
    elem = int(input("Digite um elemento da lista:"))
    lista.append(elem)
    i+=1
    #escreve a lista
    print(lista)
    #chama a função
    insertion_sort(lista)
    #escreve novamente a lista em crescente
    print(lista)
