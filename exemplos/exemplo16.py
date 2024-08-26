def lernotas():
    n=float(input("Digite uma nota para o aluno(a): "))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("NOta 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    elif media >= 4:
        n3 = float(input("\nDigite a nota da recuperação: "))
        media = (media + n3) / 2
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a,b)