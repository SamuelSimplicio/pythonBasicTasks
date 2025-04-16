#Fatoria

n = int(input("Entre com um número inteiro: "))

fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
#     fatorial *= i # Outra forma de escrever o mesmo código

print(f"O fatorial de {n} é: {fatorial}")
# O fatorial de um número é o produto de todos os números inteiros positivos até esse número.