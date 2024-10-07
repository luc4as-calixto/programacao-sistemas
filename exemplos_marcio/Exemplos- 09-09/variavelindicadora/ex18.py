n = int(input("Digite um número onteior positivo: "))
if n <= 1:
    print("Não é primo, números menores ou iguais a 1 não são considerados primos")
else:
    numero = 2
    primo = True #primo é a variável indicadora

    while (numero <= n-1):
        if(n % numero == 0) : #se n é divisível por numero
            primo = False
            break
        numero = numero + 1

    if(primo):
        print("É primo")
    else:
        print("Não é primo")