import random

def busqueda(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__":
    tamano = int(input('Cantidad de elementos: '))
    objetivo = int(input('Que numero deseas encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano)]
    encontrado = busqueda(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}')