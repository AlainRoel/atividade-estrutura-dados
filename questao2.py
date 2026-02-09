# Questão 2 - Implemente uma função recursiva em Python
def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)


n = int(input("Digite um número inteiro positivo: "))
print("Resultado:", soma_recursiva(n))
