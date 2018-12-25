# Conjuntos de pares ordenados
X = [[0, 3, 6, 9], [0, 5, 7, 8, 9]]
Y = [[2, 5, 3], [7, 1, 4, 6]]


# Funciones por tramos
def f(x):
    f = X[0]
    for i in range(len(f) - 1):
        if x > f[i] and x <= f[i+1]:
            return Y[0][i]
    return 0

def g(x):
    g = X[1]
    for i in range(len(g) - 1):
        if x > g[i] and x <= g[i+1]:
            return Y[1][i]
    return 0


# Obtengo particion de abscisa de particion final
x = []
for i in range(len(X)):
    for j in range(len(X[i])):
        x.append(X[i][j])

# Elimino elementos repetidos
x = set(x)


# Realizo la suma
final = []

for i in x:
    final.append(f(i) + g(i))

print(x)
print(final)
