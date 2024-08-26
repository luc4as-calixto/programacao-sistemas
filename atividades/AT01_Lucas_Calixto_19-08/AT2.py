#Essa parte ele vai fazer perguntas para o código funcionar
deslocamento = int(input("Digite o deslocamento: "))
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""

#Essa é a parte que ele vai criptografar as letras ou a frase que você digitou
for letra in texto:
    if letra.isupper():
        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
    elif letra.islower():
        letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)
    else: 
        letra_criptografada = letra 
    texto_criptografado += letra_criptografada

#Vai digitar a frase criptografada
print("Texto criptografado:", texto_criptografado)