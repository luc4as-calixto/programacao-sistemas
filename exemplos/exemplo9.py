notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informa a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação

if mediafinal >= 7.0:
    print("A média: %.2f - Aprovado "% mediafinal)

elif mediafinal <= 6.9 and mediafinal >= 5:
    print("A média: %.2f - Exame "% mediafinal)
    exame = float(input("Informe a nota do exame: "))
    mediafinal = (mediafinal + exame) / 2

    if mediafinal >= 7:
        print("A média: %.2f - Aprovado "% mediafinal)

    else:
        print("A média: %.2f - Reprovado "% mediafinal)

else:
    print("A média: %.2f - Reprovado "% mediafinal)