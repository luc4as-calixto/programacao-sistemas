def potencia(a, b):
    resultado = 1

    for i in range(b):
        resultado = a * resultado

    return resultado

resultado = potencia(2, 3)
print(f"A potência de 2 elevado a 3 é {resultado}.")    