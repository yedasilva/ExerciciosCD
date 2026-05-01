# Leia uma linha da entrada padrão contendo um texto
# Imprima na saída padrão uma linha contendo o mesmo text, mas com todos os caracteres em maiúsculo.

# Modificações
# Modifique o programa anterior para ler várias linhas.
# O programa para quando ler uma linha em branco.

while True:
    s = input()
    if not s:
        break
    s = s.upper()
    print(s)
