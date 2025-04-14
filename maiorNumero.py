
def maior_recursao(num, n):
    if n == 1:
        return num[0]
    else:
        return max(num[n-1], maior_recursao(num, n-1))
    
num = []

qtd = int(input("Quantos números você quer adicionar? "))
for i in range(qtd):
    n = int(input("Digite um número: "))
    # Adiciona o número à lista
    num.append(n)

# verifica qual o maior numero da lista
maior = num[0]
for i in range(1, len(num)):
    if num[i] > maior:
        maior = num[i]

#verifica qual o maior numero atraves de max   
maior2 = max(num)
# Exibe a lista de números

#verifica quem é o maior com recursão

maior3 = maior_recursao(num, len(num))
print(f"A lista de números é: {num}")

# Exibe o maior número
print(f"O maior número é: {maior}")
print(f"O maior número é: {maior2}")
print(f"O maior número é: {maior3}")
