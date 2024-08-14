# Determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo
# automóvel e o total de combustível gasto.

distancia_total = float(input("Digite o a distância total:"))
combustivel = float(input("Digite o combustível usado na viagem:"))

media = distancia_total / combustivel

print(f"A media da distância {distancia_total} e combustível {combustivel} é: {media}")
