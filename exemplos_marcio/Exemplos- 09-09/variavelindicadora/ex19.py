n = int(input("Digite uma quantidade de números: "))
anterior = int(input())

i = 1 # leu um número
ordenado = True # ordenado é a variável indicadora

while(i < n) and (ordenado):
    atual = int(input())
    i = i + 1 # leu mais um número
    if(atual < anterior):
        ordenado = False
    anterior = atual

if(ordenado):
    print("Sequência ordenada")
else:
    print("Sequência não ordenada")