def posOuNeg(numero):
    if numero < 0:
        return "N"
    elif numero > 0:
        return "P"
    else:
        return "Z"

numero = int(input("Digite um número: "))
resultado = posOuNeg(numero)
print(f"O resultado é: {resultado}")