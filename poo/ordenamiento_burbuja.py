import random

def burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n-i-1):  # 0(n) * 0(n) = o(n**2)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


if __name__ == "__main__":
    n = int(input('Cuantos elementos tiene la lista?  '))
    lista = [random.randint(0, 100) for i in range(n)]
    ordenada = burbuja(lista)
    print(ordenada)