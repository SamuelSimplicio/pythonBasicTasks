
def soma(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    if valor2 == 0:
        return "Divisão por zero não é permitida."
    return valor1 / valor2


while True:
    valor1 = int(input("Entre com um numero inteiro: "))
    valor2 = int(input("Entre com outro numero inteiro: "))

    operacao = input("Entre com a operação desejada (+, -, *, /): ")

    if operacao == "+":
        resultado = soma(valor1, valor2)
    elif operacao == "-":
        resultado = subtracao(valor1, valor2)
    elif operacao == "*":
        resultado = multiplicacao(valor1, valor2)
    elif operacao == "/":
        resultado = divisao(valor1, valor2)
    else:
        resultado = "Operação inválida."

    print(f"O resultado da operação {valor1} {operacao} {valor2} é: {resultado}")
    # A função soma recebe dois números inteiros e retorna a soma deles.