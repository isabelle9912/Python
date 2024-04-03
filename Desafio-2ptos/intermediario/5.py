#Soma de Números em String. Implemente uma função que identifique todos os números em uma string e some seus valores. Exemplo: Dada a string "Os números são 42, 78 e 123.", a função deve retornar 243 (42 + 78 + 123).


#def buscar_numeros_na_string(string):

def soma_numeros_em_string(s):
    numeros = "0123456789"
    soma = 0
    num_atual = ""
    
    for char in s:
        if char in numeros:
            num_atual += char
        else:
            if num_atual:
                soma += int(num_atual)
                num_atual = ""
    
    if num_atual:
        soma += int(num_atual)
    
    return soma

s = "Os números são 42, 78 e 123."
print(soma_numeros_em_string(s))