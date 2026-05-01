# Leia um número inteiro, n, da entrada padrão
# Imprima na saída padrão todos os números pares entre 2 e n, inclusive n se ele for par

# Modifique o programa anterior para ler várias linhas
# O programa para quando ler uma linha com o número 0

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(2, n + 1, 2):
        print(i)
