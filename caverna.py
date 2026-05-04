import random

# Tipos de célula
VAZIO = '.'
SAIDA = 'S'
ABISMO = 'A'
OCULTO = '?'


def criar_caverna(n):
    """Cria e retorna uma matriz NxN preenchida com células vazias."""
    return [[VAZIO for _ in range(n)] for _ in range(n)]


def criar_mapa_revelado(n):
    """Cria e retorna uma matriz NxN booleana com todas as células ocultas (False)."""
    return [[False for _ in range(n)] for _ in range(n)]


def posicionar_elementos(caverna, n):
    """Posiciona aleatoriamente a saída, os abismos e o ponto de partida do jogador.

    Retorna a posição inicial do jogador como (linha, coluna).
    """
    posicoes = [(i, j) for i in range(n) for j in range(n)]
    random.shuffle(posicoes)

    # Posição inicial do jogador
    linha_jogador, coluna_jogador = posicoes[0]

    # Saída na segunda posição sorteada
    l_saida, c_saida = posicoes[1]
    caverna[l_saida][c_saida] = SAIDA

    # Abismos: aproximadamente 15% das células, no mínimo 1
    num_abismos = max(1, int(n * n * 0.15))
    for i in range(2, 2 + num_abismos):
        l_ab, c_ab = posicoes[i]
        caverna[l_ab][c_ab] = ABISMO

    return linha_jogador, coluna_jogador


def contar_abismos_adjacentes(caverna, linha, coluna, n):
    """Retorna o número de abismos adjacentes (incluindo diagonais) à célula (linha, coluna)."""
    count = 0
    for dl in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dl == 0 and dc == 0:
                continue
            nl, nc = linha + dl, coluna + dc
            if 0 <= nl < n and 0 <= nc < n and caverna[nl][nc] == ABISMO:
                count += 1
    return count


def ha_saida_adjacente(caverna, linha, coluna, n):
    """Retorna True se houver uma saída adjacente (incluindo diagonais) à célula (linha, coluna)."""
    for dl in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dl == 0 and dc == 0:
                continue
            nl, nc = linha + dl, coluna + dc
            if 0 <= nl < n and 0 <= nc < n and caverna[nl][nc] == SAIDA:
                return True
    return False


def exibir_caverna(caverna, revelado, dicas, linha_jogador, coluna_jogador, n):
    """Exibe o estado atual da caverna com névoa de guerra e a posição do jogador."""
    print()
    # Cabeçalho das colunas
    print("     ", end="")
    for j in range(n):
        print(f"{j:2} ", end="")
    print()
    print("   +" + "---" * n + "+")

    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            if i == linha_jogador and j == coluna_jogador:
                print(" @ ", end="")
            elif revelado[i][j]:
                if (i, j) in dicas:
                    print(f" {dicas[(i, j)]} ", end="")
                else:
                    print(f" {caverna[i][j]} ", end="")
            else:
                print(f" {OCULTO} ", end="")
        print("|")

    print("   +" + "---" * n + "+")


def revelar_celula(caverna, revelado, dicas, linha, coluna, n):
    """Revela uma célula, calcula e armazena dicas. Retorna o tipo da célula."""
    revelado[linha][coluna] = True
    celula = caverna[linha][coluna]

    if celula == VAZIO:
        abismos = contar_abismos_adjacentes(caverna, linha, coluna, n)
        if abismos > 0:
            dicas[(linha, coluna)] = abismos

    return celula


def exibir_dica(caverna, dicas, linha, coluna, n):
    """Exibe mensagens de dica com base no conteúdo e arredores da célula atual."""
    celula = caverna[linha][coluna]

    if celula == VAZIO:
        if (linha, coluna) in dicas:
            abismos = dicas[(linha, coluna)]
            print(f"  >> Perigo! Há {abismos} abismo(s) nas proximidades.")
        else:
            print("  >> Seguro por aqui. Nenhum abismo nas proximidades.")

        if ha_saida_adjacente(caverna, linha, coluna, n):
            print("  >> Você sente uma brisa fresca... A saída está perto!")


def obter_tamanho_caverna():
    """Solicita e valida o tamanho da caverna informado pelo jogador."""
    while True:
        try:
            n = int(input("Tamanho da caverna (entre 3 e 10): "))
            if 3 <= n <= 10:
                return n
            print("Por favor, escolha um tamanho entre 3 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def obter_movimento(n):
    """Solicita e valida o movimento do jogador (linha e coluna)."""
    while True:
        try:
            entrada = input("Mover para (linha coluna): ").strip().split()
            if len(entrada) != 2:
                print("Digite exatamente dois números separados por espaço.")
                continue
            linha, coluna = int(entrada[0]), int(entrada[1])
            if 0 <= linha < n and 0 <= coluna < n:
                return linha, coluna
            print(f"Posição inválida. Os valores devem estar entre 0 e {n - 1}.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")


def exibir_legenda():
    """Exibe a legenda dos símbolos usados no mapa."""
    print("Legenda:")
    print("  @  = Você          ?  = Desconhecido")
    print("  .  = Célula vazia  S  = Saída")
    print("  A  = Abismo        1-8 = Abismos próximos")


def jogar():
    """Loop principal do jogo."""
    print("=" * 52)
    print("      A EXPLORAÇÃO DA CAVERNA PERDIDA")
    print("=" * 52)
    print("\nVocê é um explorador preso em uma caverna!")
    print("Encontre a saída antes que as tochas se apaguem.")
    print("Cuidado com os abismos!\n")
    exibir_legenda()
    print()

    n = obter_tamanho_caverna()
    tochas = n * n

    caverna = criar_caverna(n)
    revelado = criar_mapa_revelado(n)
    dicas = {}

    linha_jogador, coluna_jogador = posicionar_elementos(caverna, n)

    # Revela a célula inicial
    revelar_celula(caverna, revelado, dicas, linha_jogador, coluna_jogador, n)

    print(f"\nCaverna {n}x{n} gerada!")
    print(f"Você tem {tochas} movimentos antes das tochas se apagarem.\n")

    game_over = False
    vitoria = False

    while not game_over:
        exibir_caverna(caverna, revelado, dicas, linha_jogador, coluna_jogador, n)
        print(f"\n  Posição atual : ({linha_jogador}, {coluna_jogador})")
        print(f"  Tochas restantes: {tochas}")

        if tochas <= 0:
            print("\nAs tochas se apagaram! Você está perdido na escuridão.")
            print("FIM DE JOGO!")
            game_over = True
            break

        print()
        linha_nova, coluna_nova = obter_movimento(n)
        tochas -= 1

        celula = revelar_celula(caverna, revelado, dicas, linha_nova, coluna_nova, n)
        linha_jogador, coluna_jogador = linha_nova, coluna_nova

        if celula == ABISMO:
            exibir_caverna(caverna, revelado, dicas, linha_jogador, coluna_jogador, n)
            print(f"\nVocê caiu em um abismo em ({linha_nova}, {coluna_nova})!")
            print("FIM DE JOGO!")
            game_over = True

        elif celula == SAIDA:
            exibir_caverna(caverna, revelado, dicas, linha_jogador, coluna_jogador, n)
            print(f"\nParabéns! Você encontrou a saída em ({linha_nova}, {coluna_nova})!")
            print("Você escapou da caverna com sucesso!")
            game_over = True
            vitoria = True

        else:
            exibir_dica(caverna, dicas, linha_jogador, coluna_jogador, n)

    if not vitoria:
        # Revela o mapa completo ao fim de jogo
        print("\nMapa completo da caverna:")
        for i in range(n):
            for j in range(n):
                revelado[i][j] = True
        exibir_caverna(caverna, revelado, dicas, linha_jogador, coluna_jogador, n)

    print("\nObrigado por jogar!")


if __name__ == "__main__":
    jogar()
