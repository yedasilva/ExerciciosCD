import math
print("Olá, mundo!")

x = 1  # int
y = 5.5  # float
z0 = "Meu texto"  # string
z1 = True  # bool
z2 = False
z3 = "Outro texto"


print(x, y, 10, 12, "linha 01", sep=', ')  # args, kwargs
print(x, y, 10, 12, "linha 02", sep='; ')
print(z0)
print(z1)
print(z2)

a = x ** 3.5
print(a)

print(math.sqrt(49))
print(z0 + z3)

# estrutura de decisão 1
if z2 == True:
    print("12" + " " + "15")
else:
    print(12 + 15)

# estrutura de decisão 2
if x == 1:
    print("12" + "15")
elif x == 2:
    print(12 + 15)
else:
    print("x não é 1 e nem 2")

# laço de repetição for
