# campo minado

# imports

def main():
    print('Campo Minado')

if __name__ == '__main__':
    main()

import random


def criar_tabuleiro(tamanho, num_minas):
    tabuleiro = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
    minas = set()

    while len(minas) < num_minas:
        mina = (random.randint(0, tamanho - 1), random.randint(0, tamanho - 1))
        minas.add(mina)

    for (linha, coluna) in minas:
        tabuleiro[linha][coluna] = '*'
        for i in range(max(0, linha - 1), min(tamanho, linha + 2)):
            for j in range(max(0, coluna - 1), min(tamanho, coluna + 2)):
                if tabuleiro[i][j] != '*':
                    if tabuleiro[i][j] == ' ':
                        tabuleiro[i][j] = '1'
                    else:
                        tabuleiro[i][j] = str(int(tabuleiro[i][j]) + 1)

    return tabuleiro, minas


def mostrar_tabuleiro(tabuleiro, revelar=False):
    for linha in tabuleiro:
        print(' '.join(linha))
    print()


def revelar_celula(tabuleiro, linha, coluna, revelado):
    if tabuleiro[linha][coluna] == '*':
        return False
    elif revelado[linha][coluna] == '-':
        revelado[linha][coluna] = tabuleiro[linha][coluna]
        if tabuleiro[linha][coluna] == ' ':
            for i in range(max(0, linha - 1), min(len(tabuleiro), linha + 2)):
                for j in range(max(0, coluna - 1), min(len(tabuleiro), coluna + 2)):
                    if revelado[i][j] == '-':
                        revelar_celula(tabuleiro, i, j, revelado)
    return True


def ganhou(tabuleiro, revelado, minas):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if revelado[i][j] == '-' and (i, j) not in minas:
                return False
    return True


def jogar():
    tamanho = 5
    num_minas = 5
    tabuleiro, minas = criar_tabuleiro(tamanho, num_minas)
    revelado = [['-' for _ in range(tamanho)] for _ in range(tamanho)]

    while True:
        mostrar_tabuleiro(revelado)
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))

        if not revelar_celula(tabuleiro, linha, coluna, revelado):
            print("Você pisou em uma mina! Game Over.")
            mostrar_tabuleiro(tabuleiro, revelar=True)
            break
        elif ganhou(tabuleiro, revelado, minas):
            print("Parabéns! Você ganhou o jogo!")
            mostrar_tabuleiro(tabuleiro, revelar=True)
            break


if __name__ == "__main__":
    jogar()
