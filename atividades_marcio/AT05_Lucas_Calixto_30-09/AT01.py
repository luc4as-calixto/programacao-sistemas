quant = int(input("Digite a quantidade de notas: "))

linhanotas = []

for i in range(quant):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    linhanotas.append(nota)
    soma = sum(linhanotas)

print(linhanotas)
print("Média: ", soma/quant)
