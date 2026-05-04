# A Exploração da Caverna Perdida

Jogo em Python no terminal em que o jogador assume o papel de um explorador preso em uma caverna subterrânea NxN e deve encontrar a única saída antes que as tochas se apaguem.

## Como Jogar

```bash
python caverna.py
```

1. Ao iniciar, defina o tamanho da caverna (entre **3** e **10**).
2. Você começa em uma posição aleatória, já revelada no mapa.
3. A cada rodada, informe a **linha** e a **coluna** para onde deseja se mover.
4. Analise as pistas deixadas pelo jogo para evitar os abismos e encontrar a saída.
5. O jogo termina quando você **encontrar a saída** (vitória), **cair em um abismo** (derrota) ou as **tochas se apagarem** (derrota).

## Legenda do Mapa

| Símbolo | Significado                          |
|---------|--------------------------------------|
| `@`     | Posição atual do jogador             |
| `?`     | Célula ainda não investigada         |
| `.`     | Célula vazia e segura                |
| `S`     | Saída da caverna                     |
| `A`     | Abismo                               |
| `1`–`8` | Número de abismos nas células vizinhas |

## Pistas

- **"Perigo! Há N abismo(s) nas proximidades."** – Pelo menos um abismo está em uma célula adjacente (incluindo diagonais).
- **"Você sente uma brisa fresca... A saída está perto!"** – A saída está em uma célula adjacente.
- **"Seguro por aqui."** – Nenhum abismo está adjacente à posição atual.

## Regras

- O tamanho da caverna é definido pelo jogador no início (N entre 3 e 10).
- O número de movimentos disponíveis (tochas) é igual a **N × N**.
- A saída e os abismos são posicionados aleatoriamente a cada partida.
- O mapa completo é revelado ao fim do jogo em caso de derrota.

## Estrutura do Código

O jogo é implementado em `caverna.py` usando **apenas funções e matrizes** (sem POO ou arquivos):

| Função                             | Descrição                                              |
|------------------------------------|--------------------------------------------------------|
| `criar_caverna(n)`                 | Cria a matriz NxN com células vazias                   |
| `criar_mapa_revelado(n)`           | Cria a matriz NxN de visibilidade (névoa de guerra)    |
| `posicionar_elementos(caverna, n)` | Posiciona saída, abismos e retorna a posição inicial   |
| `contar_abismos_adjacentes(...)`   | Conta abismos vizinhos de uma célula                   |
| `ha_saida_adjacente(...)`          | Verifica se há saída em célula adjacente               |
| `exibir_caverna(...)`              | Renderiza o mapa no terminal                           |
| `revelar_celula(...)`              | Descobre uma célula e atualiza as dicas                |
| `exibir_dica(...)`                 | Exibe as mensagens de pista da célula atual            |
| `obter_tamanho_caverna()`          | Lê e valida o tamanho da caverna                       |
| `obter_movimento(n)`               | Lê e valida o movimento do jogador                     |
| `exibir_legenda()`                 | Mostra a legenda dos símbolos                          |
| `jogar()`                          | Loop principal do jogo                                 |
