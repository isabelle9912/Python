# Questão 1
max_number: int = 10
def input_int(msg: str):
    while True:
        s = input(msg)
        try:
            return  int(s)
        except ValueError:
            print('Valor inválido. Tente novamente.')
def input_int_with_alert_max(number: int):
    escolha = ''
    if number < 1:
        print('Error. Esse é o número mínimo é 1. Tente novamete.')
        input_int('Digite o número de partidas que deseja jogar: ')
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
       n: int = input_int('Digite o número de partidas que deseja jogar: ')
       input_int_with_alert_max(n)
    return number
def main():
    n: int = input_int('Digite o número de partidas que deseja jogar: ')
    input_int_with_alert_max(n)
    print(f'Número digitado {n}')

if __name__ == '__main__':
    main()