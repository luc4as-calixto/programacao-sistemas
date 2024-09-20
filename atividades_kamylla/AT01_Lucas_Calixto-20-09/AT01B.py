string = input("Digite um texto: ")
conta = {}

for letra in string:
    if letra in conta:
        conta[letra] += 1
    else:
        conta[letra] = 1

letramais = ""

for key in conta:
    if not letramais:
        letramais = key
    elif conta[key] > conta[letramais]:
        letramais = key
print(f"A letra que mais aparece é '{letramais}' com {conta[letramais]} ocorrências")