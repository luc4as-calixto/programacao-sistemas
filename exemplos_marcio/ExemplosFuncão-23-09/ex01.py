# Mostra as n notas
notas = []
n = int(input("Digite a quantidade de notas: "))
for i in range(n):
    dado = float(input(f"digite a {i + 1}ª nota: "))
    notas.append(dado)
print(notas)

# Calcula a média
soma = 0 
for i in range(len(notas)):
    soma = soma + notas[i]
media = soma / n
print(format(media, ".1f"))