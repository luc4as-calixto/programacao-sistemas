def mdc(a, b):
    #faz o MDC
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
#solicita os números para o usuário
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
#chama a função e exibe o resultado
resultado = mdc(num1, num2)
print("MDC:", resultado)
