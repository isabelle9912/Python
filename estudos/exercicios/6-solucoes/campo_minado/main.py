# CAMPO MINADO
# Isabelle Saahirah Ribeiro de Lima

# imports
import random

def escolher_celula():
    return random.choice(['0', '*'])

def gerar_campo():
    tamanho = 5
    tabuleiro = [[''][''],[''],[''],[''],['']]
    for i in range(tamanho * tamanho):
        tabuleiro.append(escolher_celula())
    print(tabuleiro)
    for i in range(5):
        for j in range(5):
            tabuleiro[i]



def main():
    print('Campo Minado')
    gerar_campo()


if __name__ == '__main__':
    main()
