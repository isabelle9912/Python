# Ler o número do mês e imprimir o número de dias que esse mês possui. P.ex: se o usuário entrar com mês 1 (janeiro) o programa deverá imprimir 31 dias, mês 2 (fevereiro) => 28 dias.

# Função para selecionar os dados do número dado pelo usuário
def selecionar_mes(mes: int) -> str:
    meses = {
        1: {"nome": "janeiro", "dias": 31},
        2: {"nome": "fevereiro", "dias": 30},
        3: {"nome": "março", "dias": 31},
        4: {"nome": "abril", "dias": 30},
        5: {"nome": "maio", "dias": 31},
        6: {"nome": "junho", "dias": 30},
        7: {"nome": "julho", "dias": 31},
        8: {"nome": "agosto", "dias": 31},
        9: {"nome": "setembro", "dias": 30},
        10: {"nome": "otubro", "dias": 31},
        11: {"nome": "novembro", "dias": 30},
        12: {"nome": "dezembro", "dias": 31},
    }
    # Imprimindo o mes e os dias de acordo com o número digitado pelo usuário
    print(f'O mês é {meses[mes]["nome"]} e tem {meses[mes]["dias"]}')

    # Fazendo o caso de exeção
    if mes not in meses:
        raise Exception("O número do mês deve estar entre 1 e 12")


# Chamando a função para múltiplos casos
selecionar_mes(3)  # Saída: O mês é março e tem 31
selecionar_mes(10)  # Saída: O mês é otubro e tem 31
selecionar_mes(6)  # Saída: O mês é junho e tem 30