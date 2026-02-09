# Questão 6 - Desenvolva um programa em Python
notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Média do aluno:", media)
