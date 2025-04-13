
while True:
    try:
        n = int(input("Digite um número inteiro: "))
        if n % 2 == 0: # O operador % retorna o resto da divisão
            # Se o resto da divisão de n por 2 for 0, então n é par
            print(f"O número {n} é par.")
        else:
            print(f"O número {n} é ímpar.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    finally: # O bloco finally é executado independentemente de uma exceção ter ocorrido ou não
        # Ele é útil para garantir que certos códigos sejam executados, como fechar arquivos ou liberar recursos
        continuar = input("Deseja continuar? (s/n): ").strip().lower() 
        # Se o usuário não digitar 's', o loop será encerrado
        # O método strip() remove espaços em branco no início e no final da string
        # O método lower() converte a string para minúsculas
        # Isso garante que o programa funcione mesmo que o usuário digite 'S' ou 'N'
        if continuar != 's':
            break