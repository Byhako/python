import random

# vamos dividiendo la lista en dos, y miramos en cual mitad esta el objetivo
def busqueda(lista, comienzo, final, objetivo):
    print(comienzo, final)
    print(f'entre {lista[comienzo]} y {lista[final - 1]}')
    # La lista debe ser ordenada
    if comienzo > final or comienzo == final or objetivo > lista[final- 1] or objetivo < lista[comienzo]:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda(lista, medio+1, final, objetivo)
    else:
        return busqueda(lista, comienzo, medio-1, objetivo)


if __name__ == "__main__":
    tamano = int(input('Cantidad de elementos: '))
    objetivo = int(input('Que numero deseas encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano)])
    encontrado = busqueda(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}')