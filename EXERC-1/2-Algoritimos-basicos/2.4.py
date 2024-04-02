#Ler o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o
#salário fixo e salário no final do mês.

def comissao(vendas: int) -> float:
    return vendas * 0.15

nome = input('Digite o nome do vendedor:')
salario_fixo = float(input(f'Digite o salário fixo de {nome}'))
total_de_vendas = int(input(f'Digite o total de vendas de {nome}'))

comissao = comissao(total_de_vendas)
salario_final = salario_fixo + comissao

print(f'O salário final de {nome} é de {salario_final}')