def dobrar_lista(lista):
    #cria uma lista nova
    nova_lista = []
    #multiplica por 2 os elementos digitados
    for elemento in lista:
        novo_elemento = elemento * 2
        #cria uma nova lista
        nova_lista.append(novo_elemento)
    #retorna o resultado
    return nova_lista

#inicializa uma lista
lista=list()
i=1
#faz as 10 perguntas para o usuário e adiciona o na lista 
while i<=10:
    elem = int(input("Digite um elemento da lista:"))
    lista.append(elem)
    i+=1
#escreve a lista
print(lista)
#coloca a função na variável só que com os números dobrados
nova_lista = dobrar_lista(lista)
#escreve a nova lista
print(nova_lista)