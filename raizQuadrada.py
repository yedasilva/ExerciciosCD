# raiz quadrada

""" n = int(input())

p = 10**-6
raiz = n

while(True):
    raiz_antiga = raiz
    raiz = (raiz + n/raiz)/2 #Método de Newton

    d = raiz_antiga - raiz
    if (d >= 0 and d < p) or (d <= 0 and d > -p):
        break
print("Raiz de {} é {}".format(n, raiz))

 """

# Usando função

n1, n2 = map(int, input().split())

def raizquadrada(n):
    p = 10**-6

    raiz = n
    while(True):
        raiz_antiga = raiz
        raiz = (raiz + n/raiz)/2 #Método de Newton

        d = raiz_antiga - raiz
        if (d >= 0 and d < p) or (d <= 0 and d > -p):
            break
    return raiz

raiz1 = raizquadrada(n1)
raiz2 = raizquadrada(n2)

print("Raiz de {} é {}".format(n1, raiz1))
print("Raiz de {} é {}".format(n2, raiz2))
