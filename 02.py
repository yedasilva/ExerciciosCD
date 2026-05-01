# Leia um número inteiro da entrada padrão.
# Imprima na saída padrão uma linha contendo a palavra "Par" ou "Ímpar" se o número for par ou ímpar, respectivamente.

n = int(input())
if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")