# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    # Caso não haja vencedor
    return None

# Função para verificar se há um empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função principal
def jogo_da_velha():
    # Criar tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Variável para controlar o jogador atual
    jogador_atual = "X"

    # Loop principal do jogo
    while True:
        # Imprimir o tabuleiro
        imprimir_tabuleiro(tabuleiro)

        # Solicitar a posição do jogador atual
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))

        # Verificar se a posição está vazia
        if tabuleiro[linha][coluna] == " ":
            # Preencher a posição com o símbolo do jogador atual
            tabuleiro[linha][coluna] = jogador_atual

            # Verificar se há um vencedor
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor:
                print(f"O jogador {vencedor} venceu!")
                break

            # Verificar se há um empate
            if verificar_empate(tabuleiro):
                print("O jogo terminou em empate!")
                break

            # Alternar para o próximo jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")

# Executar o jogo
jogo_da_velha()