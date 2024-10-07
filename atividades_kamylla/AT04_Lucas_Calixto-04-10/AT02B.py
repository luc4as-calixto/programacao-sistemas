def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
            return tabuleiro[0][coluna]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)

        linha = int(input(f"Jogador {jogador_atual} - Digite a linha (0-2): "))
        coluna = int(input(f"Jogador {jogador_atual} - Digite a coluna (0-2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            print(f"O jogador {vencedor} venceu!")
            break

        if verificar_empate(tabuleiro):
            prin("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        print("Posição inválida. Tente novamente.")

jogo_da_velha()