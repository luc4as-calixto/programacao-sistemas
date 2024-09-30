def incrementar_contador():
    global contador
    contador = contador + 1
    return contador

def exibir_contador():
    global contador
    print("contador atualizado: ",contador)

def adicionar_na_lista(item, lista):
    global minha_lista

    n = int(input("Digite o número de elementos da lista: "))
    for i in range(n):
        item = input("Digite o elemento da lista: ")
        lista.append(item)
    return minha_lista

def exibir_lista(lista):
    print(minha_lista)

def main():
    adicionar_na_lista(item, minha_lista)
    exibir_lista(minha_lista)
    incrementar_contador()
    exibir_contador()
    incrementar_contador()
    exibir_contador()
    print("Valor atual do contador: ", contador)

contador = 0
item = ""
minha_lista = []

main()