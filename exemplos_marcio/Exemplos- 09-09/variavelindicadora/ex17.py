n = int(input("Digite um número inteiro positivo: "))
if n <= 1:
    print("Não é primo, números menores ou iguais a 1 não são considerados primos")
else:
    numero = 2
    primo = True #primo é a variável indicadora

    while (numero <= n-1) and (primo):
        if (n % numero == 0) : #se n é divisível por numero
            primo = False
        numero = numero + 1

    if(primo):
        print("É primo")
    else:
        print("Não é primo")