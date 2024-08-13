# Pedra, papel e tesoura

import random
import os

# Variáveis globais para armazenar os nomes dos jogadores e os placares
jogadores = ['', '']
placar = [0, 0]
modo_de_jogo: str = ''

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_nomes():
    jogadores[0] = input('Digite o nome do jogador 1: ')
    jogadores[1] = input('Digite o nome do jogador 2: ')
    limpar_terminal()

def mostrar_placar():
   print(f'{jogadores[0]}: {placar[0]} vitórias')
   print(f'{jogadores[1]}: {placar[1]} vitórias')

def verificar_vencedor(escolha1: str, escolha2: str):
    if (escolha1 == escolha2):
        return 0
    elif ((escolha1 == 'pedra' and escolha2 == 'tesoura') or (escolha1 == 'papel' and escolha2 == 'pedra') or (escolha1 == 'tesoura' and escolha2 == 'papel')):
        return 1  # jogador 1 ganha
    else:
        return 2  # jogador 2 ganha

def obter_escolha_do_usuario(jogador):
    escolha = input(f'{jogador}, escolha pedra, papel ou tesoura: ').lower()
    while escolha not in ['pedra', 'papel', 'tesoura']:
        escolha = input('Escolha inválida. Escolha pedra, papel ou tesoura: ').lower()
    limpar_terminal()
    return escolha

def obter_escolha_do_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])

def multiplayer():
    escolha1: str = obter_escolha_do_usuario(jogadores[0])
    escolha2: str = obter_escolha_do_usuario(jogadores[1])
    vencedor: int = verificar_vencedor(escolha1, escolha2)
    if vencedor == 0:
        print('Empate!')
    else:
        placar[vencedor - 1] += 1 # incrementando as vitórias do vencedor da partida atual
        mostrar_placar()

def singleplayer():
    escolha1 = obter_escolha_do_usuario(jogadores[0])
    escolha2 = obter_escolha_do_computador()
    print(f'O computador escolheu: {escolha2}')
    vencedor = verificar_vencedor(escolha1, escolha2)
    if vencedor == 'Empate!':
        print(vencedor)
    else:
        if vencedor == 1:
            placar[0] += 1
            print(f'{jogadores}')
        else:
            print('O computador venceu')
        mostrar_placar()

def selecionar_modo_de_jogo():
    is_dois_jogadores = input('Modo multiplayer: [yes/no]: ').lower()
    while is_dois_jogadores not in ['yes', 'no']:
        is_dois_jogadores = input('Resposta inválida. Modo multiplayer: [yes/no]: ').lower()
    limpar_terminal()
    if is_dois_jogadores == 'yes':
        modo_de_jogo = 'multiplayer'
        print(modo_de_jogo)
        obter_nomes()
        multiplayer()
    else:
        modo_de_jogo = 'singleplayer'
        singleplayer()

def jogar_outra_partida():
    is_continuar_jogando = input('Quer continuar? [yes/no]: ').lower()
    while is_continuar_jogando not in ['yes', 'no']:
        is_continuar_jogando = input('Resposta inválida. Quer continuar? [yes/no]: ').lower()
    
    limpar_terminal()
    
    if is_continuar_jogando == 'yes':
        if modo_de_jogo == 'multiplayer':
           multiplayer()
        else:
           singleplayer()
    else: return False


def main():
    limpar_terminal()
    print('PEDRA PAPEL TESOURA')
    selecionar_modo_de_jogo()
    encerrar: bool = True
    while encerrar:
        encerrar = jogar_outra_partida()

if __name__ == '__main__':
    main()