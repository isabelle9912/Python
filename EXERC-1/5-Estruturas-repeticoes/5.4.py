# Imprimir todos os anos bissextos do ano 2000 até 3000. Um (ano é bissexto quando é divisível por 400) OU
# (quando é divisível por 4, mas NÃO é divisível por 100)

for i in range(1000):
    if(((i + 2000) % 400 == 0) or (((i + 2000) % 4 == 0) and ((i + 2000) % 100 != 0) )):
        print(i + 2000)