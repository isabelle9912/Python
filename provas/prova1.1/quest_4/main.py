# PEDRA PAPEL TESOURA
import random
import functions_input
import utils

# trocar pela 3 questao

jogadores: str = ['','','','']
placar: int = [0, 0]
especial = 'cegar tesoura de meu adversario'

def verificar_especial(escolha1, escolha2):
    if (escolha1 == especial) and (escolha2 == 'tesoura'):
        return 1
    elif (escolha2 == especial) and (escolha1 == 'tesoura'):
        return 2

def obter_escolha_jogador(jogador):
    escolha: str = functions_input.input_str(f'{jogador}, pedra, papel, tesoura:')
    while escolha not in ['pedra', 'papel', 'tesoura', 'cegar tesoura de meu adversario']:
        escolha: str = functions_input.input_str(f'Resposta inválida. {jogador}, pedra, papel, tesoura:')
    utils.limpar_tela()
    return escolha

def obter_escolha_computador():
    list = ['pedra', 'papel', 'tesoura']
    escolha = random.choice(list)
    return escolha

def obter_nomes(n):
    jogadores[n] = functions_input.input_str_com_comprimento_maximo(f'Digite o nome do jogador {n} ', 10)

def verificar_vencedor(escolha1: str, escolha2: str):
    if (escolha1 == escolha2):
        return 0
    elif ((escolha1 == 'pedra' and escolha2 == 'tesoura') or (escolha1 == 'papel' and escolha2 == 'pedra') or (
            escolha1 == 'tesoura' and escolha2 == 'papel')):
        return 1
    else:
        return 2

def mostrar_placar():
    print('PLACAR')
    print(f'{jogadores[0]}: {placar[0]}')
    print(f'{jogadores[1]}: {placar[1]}')

def jogar(n: int, m: int):
    escolha1 = obter_escolha_jogador(jogadores[n])
    escolha2 = obter_escolha_jogador(jogadores[m])
    isEpecial = verificar_especial()

    if (isEpecial == 1) or (isEpecial == 2):
        placar[isEpecial - 1] += 1
        return

    vencedor = verificar_vencedor(escolha1, escolha2)

    if (vencedor == 0):
        print('Empate')
    elif vencedor == 1:
        print(f'{jogadores[0]} ganhou!')
    else:
        print(f'{jogadores[1]} ganhou!')
    placar[vencedor - 1] += 1
    mostrar_placar()

def computador_vs_computador():
    escolha1: str = obter_escolha_computador()
    escolha2: str = obter_escolha_computador()
    vencedor = verificar_vencedor(escolha1, escolha2)
    placar[vencedor - 1] += 1

def obter_num_de_partidas():
    n: int = functions_input.input_int('Quantas partidas os computadores vão jogar?: ')
    return utils.input_int_with_alert_max(n)

def verificar_tipo_de_jogador():
    if (jogadores[0] == 'computador' and jogadores[1] == 'computador' and jogadores[2] == 'computador' and jogadores[3] == 'computador'):
        num_partidas: int = obter_num_de_partidas()
        for i in range(num_partidas):
            computador_vs_computador()
            computador_vs_computador()
        mostrar_placar()
        print('Fim de Jogo!')
        exit()

def seleciona_modo_de_jogo():
    print('Time 1')
    obter_nomes(0)
    obter_nomes(1)

    utils.limpar_tela()

    print('Time 2')
    obter_nomes(2)
    obter_nomes(3)

    utils.limpar_tela()

    verificar_tipo_de_jogador()

    jogar(0, 2)
    utils.limpar_tela()
    jogar(1, 3)

def jogar_outra_partida():
    opcao: str = input('Jogar outra partida? [y, n]: ')
    while opcao not in ['y', 'n']:
        opcao: str = input('Resposta inválida. Jogar outra partida? [y, n]: ')
    utils.limpar_tela()
    if opcao == 'y':
        jogar(0, 2)
        jogar(1, 3)
        return True
    else:
        return False

def main():
    utils.limpar_tela()
    print('PEDRA PAPEL TESOURA')
    seleciona_modo_de_jogo()
    encerrar: bool = True
    while encerrar:
        encerrar = jogar_outra_partida()


if __name__ == '__main__':
    main()