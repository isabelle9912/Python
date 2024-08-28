# Isabelle Saahirah Ribeiro de Lima

# Questão 2

# Estou utilizando um código que fiz em casa. Vou implementar o que foi pedido na questão, mas as feat's que fiz anteriormente serão mantidas.

import random
import time

def criar_tabuleiro(tamanho, num_minas):
    tabuleiro = [[' ' for _ in range(tamanho)] for _ in range(tamanho)] # define o tamanho do tabuleiro

    minas = set() 
    
    while len(minas) < num_minas: # preencher as minas no tabuleiro enquanto a quantidade nao chegar no número de minas definidos com base na dificuldade

        mina = (random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)) # Gera a uma posição aleatória para colocar as minas

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

def mostrar_tabuleiro(tabuleiro): # mostar o tabuleiro real, note que não é o que está na camada do usuário

    for linha in tabuleiro:
        print(' '.join(linha))

    print()

def revelar_celula(tabuleiro, linha, coluna, revelado):
    if tabuleiro[linha][coluna] == '*': # Caso de ter uma bomba
        return False 

    elif revelado[linha][coluna] == '-': # Caso da posição não tiver revelada ainda
        revelado[linha][coluna] = tabuleiro[linha][coluna] # passa o valor real para o tabuleiro visual

        if tabuleiro[linha][coluna] == ' ': # se a posição escolhida estiver vazia, verifica quantas bombas tem ao redor
            for i in range(max(0, linha - 1), min(len(tabuleiro), linha + 2)):
                for j in range(max(0, coluna - 1), min(len(tabuleiro), coluna + 2)):

                    if revelado[i][j] == '-':
                        revelar_celula(tabuleiro, i, j, revelado) # chama revelar_celula novamente para fazer a mesma verificação

    return True

def ganhou(tabuleiro, revelado, minas): # verifica se o usuário já ganhou a partida varrendo as celulas do tabuleiro visual buscando por minas escondidas, se não tiver, retorna True

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):

            if revelado[i][j] == '-' and (i, j) not in minas:

                return False

    return True

def escolher_dificuldade(): # Define o nível de dificuldade com base na quantidade de minas que serão dispostas no tabuleiro

    while True:
        print("Escolha um nível de dificuldade:")
        print("1 - Fácil (5 minas)")
        print("2 - Médio (10 minas)")
        print("3 - Difícil (15 minas)")
        escolha = input("Digite o NÚMERO da dificuldade: ")

        if escolha == "1":
            return 5
        elif escolha == "2":
            return 10
        elif escolha == "3":
            return 15
        else:
            print("Escolha inválida, tente novamente.")

def obter_nome_jogador(): # Deixa o nome como opcional
    nome: str = input("Digite o seu nome: ")
    return nome if nome else "Jogador"

def obter_numero_partidas():
    while True:
        try:
            numero: int = int(input("Quantas partidas deseja jogar? "))
            if numero > 0:
                return numero # sai da função retornando o número de partidas
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def solicitar_proxima_partida(): # Verificar se o usuário que jogar outra partida
    while True:
        resposta = input("Deseja jogar a próxima partida? (S/N): ").strip().lower()
        if resposta in ['s', 'n']: # verificar se a resposta á válida
            return resposta == 's'
        print("Opção inválida. Tente novamente.")

def obter_posicao_valida(tamanho, tipo):
    while True:
        try:
            posicao = int(input(f"Digite a {tipo} (0 a {tamanho-1}): "))
            if 0 <= posicao < tamanho: # verificação na validade da linha e coluna
                return posicao
            else:
                print(f"Por favor, digite um número entre 0 e {tamanho-1}.")
        except ValueError: # Tratamento de erro
            print("Entrada inválida. Digite um número.")

def jogar():
    nome_jogador = obter_nome_jogador() # Obter o nome do jogador
    
    numero_partidas = obter_numero_partidas() # Obter o número de partidas
    
    vitorias = 0
    derrotas = 0
    
    for partida in range(1, numero_partidas + 1):
        print(f"\n--- Partida {partida} de {numero_partidas} ---")
        
        tamanho = 5 # Definindo o tamanho do campo minado
        
        num_minas = escolher_dificuldade() # Obter o número de com base na dificuldade

        tabuleiro, minas = criar_tabuleiro(tamanho, num_minas) # passando como o campo minado será definido com base no tamanho e números de minas
        
        revelado = [['-' for _ in range(tamanho)] for _ in range(tamanho)] # Tabuleiro visual

        inicio_partida = time.time() # pegar o tempo inicial da partida

        while True:
            mostrar_tabuleiro(revelado) # mostrar o tabuleiro
            linha = obter_posicao_valida(tamanho, "linha")  # Obter a linha
            coluna = obter_posicao_valida(tamanho, "coluna") # Obter a coluna

            if not revelar_celula(tabuleiro, linha, coluna, revelado): # se o retorno de revelar_celula for falso, então encerra a partida
                print("Você pisou em uma mina! Game Over.")
                mostrar_tabuleiro(tabuleiro) # Mostra o tabuleiro final
                derrotas += 1 # incramenta derrotas
                break
            elif ganhou(tabuleiro, revelado, minas): # Caso de vitória
                print("Parabéns! Você ganhou o jogo!")
                mostrar_tabuleiro(tabuleiro) # Mostra o tabuleiro final
                vitorias += 1 # incramenta vitórias
                break

        fim_partida = time.time() # obtem o tempo da final da partida
        
        duracao_partida = fim_partida - inicio_partida # calculo do tempo final da partida
        
        print(f"Duração da partida: {duracao_partida:.2f} segundos")
        
        print(f"Placar parcial: {nome_jogador} {vitorias} Vitórias | {derrotas} Derrotas")

        if partida < numero_partidas and not solicitar_proxima_partida(): # verifica se tem mais partidas para jogar
            break

    print(f"\n--- Placar Final ---\n{nome_jogador}: {vitorias} Vitórias | {derrotas} Derrotas")
    
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()
