n = int(input("Digite um número inteiro positivos: "))
if n <= 1:
    print("Não é primo, números menores ou iguais a 1 não são considerados primos")
else:
    numero = 2
    divisores = 0 #divisores é a variável contadora

    while(numero <= n-1):
        if(n % numero == 0): #se n é divisível por numero
            divisores = divisores + 1
        numero = numero + 1

    if(divisores == 0):
        print("É primo")
    elif(divisores == 1):
        print("Não é primo. Possui 1 divisor diferente 1 e {}".format(n))
    else:
        print("Não é primo. Possui {} divisores diferentes de 1 e {}".format(divisores, n))