#Ler o preço de compra e o percentual de lucro desejado por um vendedor, no final o programa deverá
#calcular e imprimir o preço de venda.

def calcular_lucro(valor_compra: float, valor_percentual: float) -> float:
    return valor_compra * (valor_percentual/100)

preco = float(input('Digite o valor da compra:'))
percentual = float(input(f'Digite o percentual de lucro que deseja aplicar na compra de {preco}'))

valor_final = calcular_lucro(preco, percentual)

print(f'O valor final do produto é {valor_final}')