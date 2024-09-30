def fatorial(n, resultado=1):
    
# Função que lê um número inteiro n >= 0 e imprime n!
    if n == 0 or n == 1: # caso base
        return resultado
    #faz a fatorial
    else: 
        return fatorial(n - 1, n * resultado)
# Função principal
def main():
    #pede um número ao usuário
    n = int(input("Digite um número inteiro: "))
    #guarda o resultado da função 
    resultado = fatorial(n)
    #escreve o resultado
    print(20*"#")
    print("Fatorial:", resultado)
    print(20*"#") 
main()