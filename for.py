notas = []

for i in range(3):
    codigo_aluno = input("Digite o código do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    resultado = (codigo_aluno, nota)
    notas.append(resultado)

print("quantidade de notas:", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM do aluno é:", codigo_aluno, "e a nota é:", nota)
