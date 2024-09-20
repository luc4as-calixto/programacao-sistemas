n = int(input("Digite a quantidade desejada de números: "))
anterior = int(input())

i = 1 #leu um número 
adjacentes = False

while (i < n):
    atual = int(input())
    i = i + 1 #leu mais um número
    if (atual == anterior):
        adjacentes = True
    anterior = atual

if(adjacentes == True):
    print("Tem dois números adjacentes iguais")
else:
    print("Não tem dois números adjacente iguais")
