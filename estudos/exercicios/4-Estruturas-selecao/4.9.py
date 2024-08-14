# Jogo “pedra-papel-tesoura”, o usuário compete com o computador. O usuário entra com a sua arma,
# “pedra”, “papel” ou “tesoura”. Em seguida, o programa imprime: “Você Venceu!” (usuário), “Eu Venci”
# (computador) ou “Empate”. Lembretes: pedra ganha de tesoura, tesoura ganha de papel e papel ganha de
# pedra

import random
import os

opcao = 1

while opcao > 0:
    opcao = int(
        input("Escolha sua arma: (1 = PEDRA) (2 = PAPEL) (3 = TESOURA) (-1 = SAIR): ")
    )
    escolha_aleatoria = random.randint(
        1, 3
    )  # passando minimo e maximo para a escolha de número aleatório
    os.system("clear")

    if opcao == 1:  # PEDRA
        if escolha_aleatoria == 1:
            print("EMPATE!")
        if escolha_aleatoria == 2:
            print("DERROTA!")
        if escolha_aleatoria == 3:
            print("VITÓRIA!")

    if opcao == 2:  # PAPEL
        if escolha_aleatoria == 1:
            print("VITÓRIA!")
        if escolha_aleatoria == 2:
            print("EMPATE!")
        if escolha_aleatoria == 3:
            print("DERROTA!")

    if opcao == 2:  # TESOURA
        if escolha_aleatoria == 1:
            print("DERROTA!")
        if escolha_aleatoria == 2:
            print("VITÓRIA!")
        if escolha_aleatoria == 3:
            print("EMPATE!")
