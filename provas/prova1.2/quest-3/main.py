# Isabelle Saahirah Ribeiro de Lima

# Questão 3

def main():
    print("============================================================")
    print("Jogo Pedra-Papel-Tesoura")
    print()	

     # Captura dos nomes dos jogadores
    jogador1 = 'Tabosa'
    jogador2 = 'Coxinha'
    jogador3 = 'Doquinha'

    # Inicialização dos placares
    placar = {jogador1: 1, jogador2: 0, jogador3: 0}
    num_empates = 0

    # Definir o número de partidas
    num_partidas = 1
    print()

    for partida in range(1, num_partidas + 1):
        print(f"--- Partida {partida} de {num_partidas} ----------------------------------------------------------")

        # Escolhas dos jogadores
        escolha1 = 'Tesoura'
        escolha2 = 'Papel'
        escolha3 = 'Papel'

        vencedor_final = jogador1


        print(f"\nPlacar:\n{vencedor_final} ......: {placar[vencedor_final]} !! Vencedor da partida !!\n")


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
if __name__ == '__main__':
    main()