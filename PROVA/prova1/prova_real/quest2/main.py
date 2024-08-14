# PEDRA PAPEL TESOURA
import os
import random

jogadores: str = ['', '']
placar: int = [0, 0]
modo_de_jogo: str = ['', '']
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def input_str(msg: str):
    s = input(msg)
    if s.strip() != '':
        return s
    print('A entrada não pode ser vazia! Tente novamente.')

def input_str_com_comprimento_maximo(msg: str, max_len: int | None = None) -> str:
    while True:
        s = input_str(msg)  # chama a função input_str() definida acima
        if (max_len is None) or (len(s) <= max_len):
            return s
        print(f'Entrada muito longa! Máximo de {max_len} caracteres. Tente novamente.')

def obter_escolha_jogador(jogador):
    escolha: str = input_str(f'{jogador}, pedra, papel, tesoura:')
    while escolha not in ['pedra', 'papel', 'tesoura']:
        escolha: str = input_str(f'Resposta inválida. {jogador}, pedra, papel, tesoura:')
    limpar_tela()
    return escolha
def obter_escolha_computador():
    # global dificuldade
    # if dificuldade == 'easy':
    list = ['pedra', 'papel', 'tesoura']
    escolha = random.choice(list)
    return escolha
def obter_nomes(n):
    jogadores[n] = input_str_com_comprimento_maximo('Digite o nome do jogador: ', 10)

def verificar_vencedor(escolha1: str, escolha2: str):
    if(escolha1 == escolha2):
        return 0
    elif ((escolha1 == 'pedra' and escolha2 == 'tesoura') or (escolha1 == 'papel' and escolha2 == 'pedra') or (escolha1 == 'tesoura' and escolha2 == 'papel')):
        return 1
    else:
        return 2

def mostrar_placar():
    print('PLACAR')
    print(f'{jogadores[0]}: {placar[0]}')
    print(f'{jogadores[1]}: {placar[1]}')
def multiplayer():
    escolha1 = obter_escolha_jogador(jogadores[0])
    escolha2 = obter_escolha_jogador(jogadores[1])
    vencedor = verificar_vencedor(escolha1, escolha2)

    if(vencedor == 0):
        print('Empate')
    elif vencedor == 1:
        print(f'{jogadores[0]} ganhou!')
    else:
        print(f'{jogadores[1]} ganhou!')
    placar[vencedor - 1] += 1
    mostrar_placar()
def singleplayer():
    escolha1: str = obter_escolha_jogador(jogadores[0])
    escolha2: str = obter_escolha_computador()
    print(f'O computador escolheu {escolha2}')
    vencedor = verificar_vencedor(escolha1, escolha2)

    if(vencedor == 0):
        print('Empate!')
    elif (vencedor == 1):
        print(f'{jogadores[0]} ganhou!')
    else:
        print('O computador ganhou')
    placar[vencedor - 1] += 1
    mostrar_placar()

def seleciona_modo_de_jogo():
    global modo_de_jogo
    is_multiplayer: str = input('Deseja jogar multiplayer? [y, n]: ')
    while is_multiplayer not in ['y', 'n']:
        is_multiplayer: str = input('Resposta inválida. Deseja jogar multiplayer? [y, n]: ')
    if is_multiplayer == 'y':
        modo_de_jogo = 'multiplayer'
        obter_nomes(0)
        obter_nomes(1)
        multiplayer()
    else:
        modo_de_jogo = 'singleplayer'
        obter_nomes(0) # nome para o usuário
        jogadores[1] = 'computador'

def jogar_outra_partida():
    global modo_de_jogo
    opcao: str = input('Jogar outra partida? [y, n]: ')
    while opcao not in ['y', 'n']:
        opcao: str = input('Resposta inválida. Jogar outra partida? [y, n]: ')
    limpar_tela()
    if opcao == 'y':
        if modo_de_jogo == 'multiplayer':
            multiplayer()
        else:
            singleplayer()
        return True
    else: return False
def main():
    limpar_tela()
    print('PEDRA PAPEL TESOURA')
    seleciona_modo_de_jogo()
    encerrar: bool = True
    while encerrar:
        encerrar = jogar_outra_partida()

if __name__ == '__main__':
    main()