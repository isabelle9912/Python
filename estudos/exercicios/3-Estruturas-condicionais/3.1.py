# Ler um número inteiro e informar se este valor é maior #que 10.


def is_maior(a: int):
    if a > 10:
        return "é maior"
    else:
        return "não é maior"


num = int(input("Digite um número "))

s = is_maior(num)
print(f"o número {num} {s}")
