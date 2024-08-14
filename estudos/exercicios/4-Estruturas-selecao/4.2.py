# Refaça o exercício anterior, MAS o usuário deve entrar com o nome do mês e o programa tem como saída o
# número correspondente ao mês lido. P.ex. se o usuário digitou “janeiro” o programa imprime mês 1.


def selecionar_mes(mes: str):
    meses = {
        "janeiro": 1,
        "fevereiro": 2,
        "março": 3,
        "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        "agosto": 8,
        "setembro": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12,
    }

    if mes.lower() in meses:
        print(meses[mes.lower()])
    else:
        raise Exception("Nome de mês inválido!")


# chamando a função para múltiplos casos
selecionar_mes("dezembro")
selecionar_mes("janeiro")
selecionar_mes("outubro")
selecionar_mes("asds")
