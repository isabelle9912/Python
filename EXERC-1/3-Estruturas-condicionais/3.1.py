#Ler um número inteiro e informar se este valor é maior #que 10.

def is_par(a: int):
    if(a % 2 == 0):
        return 'Par'
    else:
        return 'Ímpar'        

num = int(input('Digite um número '))
s = is_par
print(s)

