n1 = lerNumeroInt()
n2 = lerNumeroInt()
res = soma(n1, n2)
print("A soma é:", res)

def lerNumeroInt():
    numero = input("Digite um número inteiro: ")
    return int(numero)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# O erro acontence porque a função lerNumeroInt() é chamada antes de ser definida.
# Para corrigir o erro, basta inverter a ordem das funções. Primeiro defina a função lerNumeroInt() e depois chame a função.