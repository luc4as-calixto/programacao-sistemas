def lerNumeroInt():
    numero = input("Digite um número inteiro: ")
    return int(numero)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

n1 = lerNumeroInt()
n2 = lerNumeroInt()
res = soma(n1, n2)
print("A soma é:", res)
print("A soma é:", soma(3, 5))	