#Similar à questão anterior, mas informe se o número digitado é maior, menor ou igual a 10.

def is_maior(a: int):
    if(a > 10):
        return 'é maior'
    if(a == 10):
        return 'é igual'
    else:
        return 'não é maior'        



num = int(input('Digite um número '))

s = is_maior(num)
print(f'o número {num} {s}')