def obter_ultimo_elemento(lista):
    #retorna com o último digito da lista
    if lista:
        return lista[-1]
    else: 
        return None

#cria uma lista
lista=list()
i=1
#faz as 10 perguntas ao usuário e coloca na lista
while i<=5:
    elem = int(input("Digite um elemento da lista:"))
    lista.append(elem)
    i+=1
    #escreve a lista
    print(lista)
    #chama a função e coloca o resultado na variável
    ultimo_elemento = obter_ultimo_elemento(lista)
    #escreve o resultado da função
    print("Último elemento da lista:", ultimo_elemento)