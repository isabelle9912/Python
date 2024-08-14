#Transformação de String: Dada uma string, substitua cada letra pela letra oposta no alfabeto (a ↔ z, b ↔ y, c ↔ x, etc.).

# ACHAR A POSIÇÃO DA LETRA NA STRING E FAZER UM LOOP REVERSO PRA ACHAR A OPOSTA

def substituir_letras_opostas(string):
  
    opostas = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
        'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
        'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a'
    }
    
  
    result= ""
    
    # Loop sobre cada letra na string
    for let in string:
        # Se a letra estiver no dicionário, substitua pela letra oposta
        if let in opostas:
            result += opostas[let]
        else:
            # Se a letra não estiver no dicionário, mantenha-a como está
            result += let
    
    return result

# Teste da função
string = "porta"
result = substituir_letras_opostas(string)
print(result) 