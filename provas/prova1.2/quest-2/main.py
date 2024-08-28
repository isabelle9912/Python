# Isabelle Saahirah Ribeiro de Lima

# Questão 2

import random

# Função para capturar a escolha do jogador
def escolha_jogador(nome):
    while True:
        escolha = input(f"{nome}, escolha Pedra, Papel ou Tesoura: ").strip().lower()
        if escolha in ['pedra', 'papel', 'tesoura']:
            return escolha.capitalize()
        print("Escolha inválida. Tente novamente.")

# Função para determinar o vencedor entre duas escolhas
def determinar_vencedor(jogador1, escolha1, jogador2, escolha2):
    if escolha1 == escolha2:
        print(f"{jogador1} ({escolha1}) vs {jogador2} ({escolha2}). Empate!")
        return None

    if (escolha1 == 'Pedra' and escolha2 == 'Tesoura') or \
       (escolha1 == 'Papel' and escolha2 == 'Pedra') or \
       (escolha1 == 'Tesoura' and escolha2 == 'Papel'):
        print(f"{jogador1} ({escolha1}) vs {jogador2} ({escolha2}). {escolha1} vence {escolha2}. {jogador1} venceu!")
        return jogador1
    else:
        print(f"{jogador1} ({escolha1}) vs {jogador2} ({escolha2}). {escolha2} vence {escolha1}. {jogador2} venceu!")
        return jogador2

# Função principal do jogo
def jogar():
    print("============================================================")
    print("Jogo Pedra-Papel-Tesoura")
    print()

    # Captura dos nomes dos jogadores
    jogador1 = input("Digite o nome do Jogador-1: ")
    jogador2 = input("Digite o nome do Jogador-2: ")
    jogador3 = input("Digite o nome do Jogador-3: ")

    # Inicialização dos placares
    placar = {jogador1: 0, jogador2: 0, jogador3: 0}
    num_empates = 0

    # Definir o número de partidas
    num_partidas = int(input("Número de partidas? "))
    print()

    for partida in range(1, num_partidas + 1):
        print(f"--- Partida {partida} de {num_partidas} ----------------------------------------------------------")

        # Escolhas dos jogadores
        escolha1 = escolha_jogador(jogador1)
        escolha2 = escolha_jogador(jogador2)
        escolha3 = escolha_jogador(jogador3)

        # Determinação do vencedor da primeira rodada
        vencedor_round1 = determinar_vencedor(jogador1, escolha1, jogador2, escolha2)

        # Se houve empate na primeira rodada
        if vencedor_round1 is None:
            vencedor_final = determinar_vencedor(f"{jogador1} e {jogador2}", escolha1, jogador3, escolha3)
        else:
            vencedor_final = determinar_vencedor(vencedor_round1, escolha1 if vencedor_round1 == jogador1 else escolha2, jogador3, escolha3)

        # Atualização do placar
        if vencedor_final:
            placar[vencedor_final] += 1
            print(f"\nPlacar:\n{vencedor_final} ......: {placar[vencedor_final]} !! Vencedor da partida !!\n")
        else:
            num_empates += 1
            print("\nPlacar: !! Empate !!\n")

        if partida < num_partidas:
            continuar = input("--- Próxima partida (S/n)? ").strip().lower()
            if continuar != 's':
                break
        print()

    # Exibição do placar final
    print("--- Placar Final, {} partidas --------------------------------------------------".format(partida))
    for jogador, pontos in placar.items():
        print(f"{jogador} ........: {pontos}")
    print(f"Núm. de empates: {num_empates}")
    vencedor_final = max(placar, key=placar.get)
    if list(placar.values()).count(placar[vencedor_final]) == 1:
        print(f"{vencedor_final} !! É o vencedor !!")
    else:
        print("Empate no placar final!")

    print("\nFim de jogo")
    print("============================================================")

if __name__ == "__main__":
    jogar()
