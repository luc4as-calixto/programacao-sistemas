#função para ver qual é o maior número
def maior3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else: 
        return c

#pergunta os números ao usuário
n1=int(input("Digite um número:"))
n2=int(input("Digite um número:"))
n3=int(input("Digite um número:"))
#chama a função e exibe o maior número
resultado = maior3(n1,n2,n3)
print(resultado)