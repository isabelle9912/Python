def input_str(msg: str):
    s = input(msg)
    if s.strip() != '':
        return s
    print('A entrada não pode ser vazia! Tente novamente.')


def input_int(msg: str):
    while True:
        s = input(msg)
        try:
            return int(s)
        except ValueError:
            print('Valor inválido. Tente novamente.')


def input_str_com_comprimento_maximo(msg: str, max_len: int | None = None) -> str:
    while True:
        s = input_str(msg)  # chama a função input_str() definida acima
        if (max_len is None) or (len(s) <= max_len):
            return s
        print(f'Entrada muito longa! Máximo de {max_len} caracteres. Tente novamente.')
