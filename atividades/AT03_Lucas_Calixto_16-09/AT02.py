texto = input("Digite um texto: ")
pontuacao = [",", ".", ";", ":", "!", "?"]

#remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p, " ")

texto = texto.replace(" ", "")

#deixa miniscula o texto
texto = texto.lower()

inversa = texto[::-1]

if texto in inversa:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")