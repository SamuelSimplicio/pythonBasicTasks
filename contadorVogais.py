def contar_vogais(palavra):
    """
    Função que conta o número de vogais em uma palavra.
    :param palavra: string
    :return: inteiro
    """
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in palavra: # Itera sobre cada letra da palavra
        # Se a letra estiver na string de vogais, incrementa o contador
        if letra in vogais:# Se a letra for uma vogal
            contador += 1
    return contador

palavra = input("Digite uma palavra: ")
quantidade_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' tem {quantidade_vogais} vogais.")