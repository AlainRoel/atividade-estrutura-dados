# Questão 1 - Desenvolva um programa em Python que:
numeros = []

for i in range(5):
    valor = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(valor)

print("Elementos da lista:", numeros)
print("Soma dos valores:", sum(numeros))
