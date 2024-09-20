string = input("Digite um texto: ")
dicionario = {}

for letra in string:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

print(f"A letra que mais aparece é: {max(dicionario, key=dicionario.get)}, que repetiu: {max(dicionario.values())} vezes.")