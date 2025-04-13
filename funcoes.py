
def minha_funcao(valor1,valor2):
    """
    Esta função recebe dois valores e retorna a soma deles.
    """
    return valor1 + valor2

while True:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado = minha_funcao(valor1, valor2)
    print("A soma é:", resultado)