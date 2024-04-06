# Imprimir todos os números divisíveis por 3 ou 7 de 1 até 1000.
j = 0
for i in range(1000):
    if(((i + 1) % 3) or ((i + 1) % 7)):
        print(i + 1)
        j += 1
