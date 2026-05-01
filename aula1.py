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
    print("Linha 2 do if")
    print("Linha 3 do if")
elif x == 2:
    print(12 + 15)
else:
    print("x não é 1 e nem 2")

# laço de repetição for
for i in range(1, 3):
    print(i)
    print("12" + "15", i)

# laço de repetição while
j = 1
while j < 3:
    print("while", j)
    j += 1

# aninhamento
for i in range(1, 3):
    print("for de fora", i)
    for j in range(1, 10, 2):
        print("--->", i, j)
        if i+j == 5:
            break


# lista

lista = [1, 3, 8, 12]
print(lista[0])
print(lista[3])

notas = [1, 3, 8, 9]
print(notas)
notas[1] = 8
print(notas)
notas.append(10)
print(notas)

for i, v in enumerate(notas):
    print(i, v)

# dicionários

notas2 = {
    "Alex": 9,
    "Debora": 9.5,
    "Pedro": "Não fez a prova",
    12: "Banana",
    "Paulo": False,
}
print(notas2)
print(notas2["Alex"])
print(notas2[12])

print(notas2)
for k, v in notas2.items():
    print(k, v) 

