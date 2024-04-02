#Ler os catetos de um triângulo retângulo e escrever sua hipotenusa. Considere a equação c² = a² + b²
#onde c é a hipotenusa, a e b os catetos.

def calcular_hipotenusa(a: float, b: float) -> float:
    c = (a ** 2 + b ** 2) ** 0.5
    return c

cateto1 = float(input('Digite o primeiro cateto:'))
cateto2 = float(input('Digite o segundo cateto:'))

hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print(f'A hipotenusa do triângulo de catetos {cateto1} e {cateto2} é {hipotenusa}')
