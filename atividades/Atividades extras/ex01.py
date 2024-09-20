def verificacao():

    nota = float(input("Digite uma nota entre 0 e 10: "))

    if (nota >= 0) and (nota <= 10):
        print("Valor válido")
    else:
        print("Valor inválido")
        verificacao()
 
verificacao()
