#Ler dois números inteiros e informar se estes números são iguais ou diferentes.

def is_equal(a: int, b: int):
    if(a > 10):
        return 'é maior'
    if(a == 10):
        return 'é igual'
    else:
        return 'não é maior'        



num1 = int(input('Digite um número '))
num2 = int(input('Digite um número '))


s = is_equal(num1, num2)
print(f'Os números {num1} e {num2} {s}')