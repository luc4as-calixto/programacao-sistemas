n = int(input("Digite uma quantidade de números: "))
anterior = int(input())

ordenado = True # ordenado é a variável indicadora

for i in range(n-1):
    atual = int(input())
    if atual < anterior:
        ordenado = False
        break
    anterior = atual

if(ordenado):
    print("Sequência ordenada")
else:
    print("Sequência não ordenada")