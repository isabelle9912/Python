# Função para ver o mês coorespondente ao num digitado OBS: é case sensitive, estamos assumindo que virá um num inteiro


def selecionar_mes(mes: int) -> str:
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }

    if mes not in meses:
        raise Exception("O número do mês deve estar entre 1 e 12")

    return meses[mes]


# Chamando a função para múltiplos casos
print(selecionar_mes(3))  # Saída: março
print(selecionar_mes(10))  # Saída: outubro
print(selecionar_mes(6))  # Saída: junho
print(selecionar_mes(-3))  # Lança uma exceção
print(selecionar_mes(0))  # Lança uma exceção
print(selecionar_mes(13))  # Lança uma exceção
