import random

def cria_matriz(tabuleiro):
    matriz = []

    for i in range(tabuleiro):
        linha = []

        for j in range(tabuleiro):
            linha.append('?')

        matriz.append(linha)

    return matriz



def matriz_copia(dicas, abismos, tabuleiro):
    copia = []

    m = 'M'
    s = 'S'
    c ='_'
    a = 'A'
    saida = 1

    copia = []

    for i in range(tabuleiro):
        elementos = []
        for j in range(tabuleiro):
            if dicas > 0:
                elementos.append('M')
                dicas -=1
            elif abismos > 0:
                elementos.append('A')
                abismos -=1
            elif saida > 0:
                elementos.append('S')
                saida -=1
            else:
                elementos.append('_')

        copia.append(elementos)

    gabarito = [item for linha in copia for item in linha]
    random.shuffle(gabarito)

    while not gabarito[0] == '_':
        random.shuffle(gabarito)

    position = 0

    for i in range(len(copia)):
        for j in range(len(copia)):
            copia[i][j] = gabarito[position]
            position += 1 

    return copia

def validarMovimento(coordenadaX, coordenadaY, mapa):
    movimentoValido = False
    if coordenadaX < 0 or coordenadaX >= len(mapa) or coordenadaY < 0 or coordenadaY >= len(mapa):
        movimentoValido = False
    else:
        movimentoValido = True

    if movimentoValido == True:
        if mapa [coordenadaX][coordenadaY] == '?':
            movimentoValido = True
        else:
            movimentoValido = False

    return movimentoValido

def buscarsaida(mapa_gabarito):
    for i in range(len(mapa_gabarito)):
        for j in range(len(mapa_gabarito)):
            if mapa_gabarito[i][j] == 'S':
               return {
                   'saidaX': i,
                   'saidaY': j
               }

def darDicas(coordenadaX, coordenadaY, mapa_gabarito):
    saida = buscarsaida(mapa_gabarito)
    saidaX = saida['saidaX']
    saidaY = saida['saidaY']

    mensagem = ""

    if coordenadaX < saidaX:
        mensagem += "A saída está para baixo. "
    elif coordenadaX > saidaX:
        mensagem += "A saída está para cima. "

    if coordenadaY < saidaY:
        mensagem += "A saída está à direita. "
    elif coordenadaY > saidaY:
        mensagem += "A saída está à esquerda. "

    return mensagem

def revelarMapa(coordenadaX, coordenadaY, mapa, mapa_gabarito, vidas, venceuJogo):
    if mapa_gabarito[coordenadaX][coordenadaY] == 'M':
        mapa[coordenadaX][coordenadaY] = 'M'
        print(darDicas(coordenadaX, coordenadaY, mapa_gabarito))

    elif mapa_gabarito[coordenadaX][coordenadaY] == 'A':
        mapa[coordenadaX][coordenadaY] = 'A'
        vidas -= 1
        print("Você caiu em um abismo!")
    elif mapa_gabarito[coordenadaX][coordenadaY] == 'S':
        mapa[coordenadaX][coordenadaY] = 'S'
        venceuJogo = True
        print("Parabéns! Você encontrou a saída e venceu o jogo!")
    else:
        mapa[coordenadaX][coordenadaY] = '_'

    input("Pressione Enter para continuar...")

    return {
        'mapa': mapa,
        'vidas': vidas,
        'venceuJogo': venceuJogo
    }

def imprimirMapa(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            print(mapa[i][j], end=' ')
        print()


if __name__ == '__main__':
    try:
        tabuleiro = int(input("Digite o tamanho do tabuleiro do jogo (5 a 10): "))

        while tabuleiro < 5 or tabuleiro > 10:
            print("Valor inválido, tente novamente")
            tabuleiro = int(input("Digite o tamanho do tabuleiro do jogo (5 a 10): "))
        
        dicas = int(input('Quantas dicas você quer que o tabuleiro tenha no total? (5 a 8)'))

        while dicas < 5 or dicas > 8:
            print("Valor inválido, tente novamente")
            dicas = int(input('Quantas dicas você quer que o tabuleiro tenha no total? (5 a 8)'))
        
        abismos = int(input('Quantos abismos você quer que o tabuleiro tenha no total? (3 a 6)'))

        while abismos < 3 or abismos > 6:
            print("Valor inválido, tente novamente")
            abismos = int(input('Quantos abismos você quer que o tabuleiro tenha no total? (3 a 6)'))
        
        mapa = cria_matriz(tabuleiro)
        mapa_gabarito = matriz_copia( dicas, abismos, tabuleiro)

        vidas = 1

        venceuJogo = False

        coordenadaX = 0
        coordenadaY= 0
        imprimirMapa(mapa)

        while vidas > 0 and not venceuJogo:
            coordenadaX = int(input("Digite as coordenada X: "))
            coordenadaY = int(input("Digite as coordenada Y: "))

            while not validarMovimento(coordenadaX, coordenadaY, mapa):
                coordenadaX = int(input("Digite as coordenada X: "))
                coordenadaY = int(input("Digite as coordenada Y: "))

            resultado = revelarMapa(coordenadaX, coordenadaY, mapa, mapa_gabarito, vidas, venceuJogo)
            mapa = resultado['mapa']
            vidas = resultado['vidas']
            venceuJogo = resultado['venceuJogo']

            imprimirMapa(mapa)

    except ValueError:
        print("Erro no sistema, digite apenas números")

