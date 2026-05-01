# Leia um número inteiro, n, da entrada padrão
# Imprima na saída padrão todos os números pares entre 2 e n, inclusive n se ele for par

n = int(input())

""" for i in range(1, n + 1):
    if i % 2 == 0:
        print(i) """

for i in range(2, n + 1, 2):
    print(i)
