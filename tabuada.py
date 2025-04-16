import os
# Tabuada

def limpa_console():
    os.system('cls' if os.name == 'nt' else 'clear')

valor = int(input("Entre com um número inteiro: "))

while True:
    opcao = input("Selecione a operação desejada (1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Outro Numero, 6 - Sair): ")

    if opcao == "1": # Adição
        for i in range(1, 11):
            resultado = valor + i
            print(f"{valor} + {i} = {resultado}")
    elif opcao == "2": # Subtração
        for i in range(1, 11):
            resultado = valor - i
            print(f"{valor} - {i} = {resultado}")
    elif opcao == "3": # Multiplicação
        for i in range(1, 11):
            resultado = valor * i
            print(f"{valor} * {i} = {resultado}")
    elif opcao == "4": # Divisão
        for i in range(1, 11):
            if i == 0:
                print("Divisão por zero não é permitida.")
            else:
                resultado = valor / i
                print(f"{valor} / {i} = {resultado}")
    elif opcao == "5": # Outro Número
        limpa_console()
        valor = int(input("Entre com um novo número inteiro: "))
    elif opcao == "6": # Sair
        limpa_console()
        print("Saindo do programa.")
        break  

