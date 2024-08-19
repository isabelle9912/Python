import os
import functions_input

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_int_with_alert_max(number: int):
    escolha = ''
    max_number = 10 # número máximo de partidas pré-definido
    if number < 1:
        print('Error. Esse é o número mínimo é 1. Tente novamete.')
        functions_input.input_int('Digite o número de partidas que deseja jogar: ')
        input_int_with_alert_max()
    elif number == max_number:
        escolha: str = input(f'Alerta. Esse é o número máximo {max_number}! Deseja continuar? [y, n]').lower()
        while escolha not in ['y', 'n']:
            escolha: str = input(f'Alerta. Esse é o número máximo {max_number}! Deseja continuar? [y, n]').lower()
    elif number > 10:
        escolha: str = input(f'Alerta. Esse é o número ultrapassa o limite de {max_number}! Deseja continuar? [y, n]').lower()
        while escolha not in ['y', 'n']:
            escolha: str = input('Resposta inválida. Esse é o número máximo! Deseja continuar? [y, n]').lower()
    if escolha == 'n':
       n: int = functions_input.input_int('Digite o número de partidas que deseja jogar: ')
       input_int_with_alert_max(n)
    return number
