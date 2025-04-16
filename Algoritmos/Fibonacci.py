
numA = 0
numB = 1
i = 0

n = int(input("Entre com um número inteiro: "))

while i < n:
    print(numA, end=", ")
    num = numA + numB
    numB = numA
    numA = num
    i += 1