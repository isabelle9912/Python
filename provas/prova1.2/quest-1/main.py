# Isabelle Saahirah Ribeiro de Lima

# Questão 1

from unicodedata import normalize

def remover_acentos(s: str) -> str:
    """ Remove os acentos de uma string. P.ex. Não => Nao (sem acento) """
    return normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')

def input_opcoes(msg: str, *opcoes: str) -> str:
    """
    Exibe uma mensagem e uma lista de opções para o usuário escolher.
    É case insensitive, então, não importa se o usuário digitar letras maiúsculas ou minúsculas.
    
    Args:
        msg (str): A mensagem a ser exibida ao usuário.
        *opcoes (str):
            Um número variável de opções que o usuário pode escolher. Similar a uma list.
            Em cada opção passada, a letra maiúscula se refere à forma curta da opção.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    opcoes_sem_acento = [remover_acentos(opcao) for opcao in opcoes]

    while True:
        entrada = input(f"{msg} ({' / '.join(opcoes)})? ")
        entrada_sem_acento = remover_acentos(entrada).strip()

        for opcao, opcao_sem_acento in zip(opcoes, opcoes_sem_acento):
            if entrada_sem_acento.lower() == opcao_sem_acento.lower() or entrada_sem_acento.lower() == opcao_sem_acento[0].lower():
                return opcao

        print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    escolha = input_opcoes('\n1. Deseja continuar', 'S', 'N')
    print(f"Você escolheu: {escolha}")

    escolha = input_opcoes('\n2. Deseja continuar', 's', 'n')
    print(f"Você escolheu: {escolha}")

    escolha = input_opcoes('\n3. Deseja continuar', 'Sim', 'Não')
    print(f"Você escolheu: {escolha}")