texto  = input("Digite um texto: ")
pontuacao = [",", ".", ";", ":", "!", "?"]

#remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p, " ")

numeropalavras = len(texto.split())
print("A quantidade de palavras é: ", numeropalavras)

#Outra forma de resolver o problema

# separa as palavreas
# texto = texto.split()
# contador = 0

# conta as palavras
# for x in texto:
#     contador = contador + 1

# print("A quantidade de palavras é: ", contador)