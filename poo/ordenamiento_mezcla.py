import random

def ordenar(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        iz = lista[:mitad]
        de = lista[mitad:]

        print(iz, '*'*5, de)

        # llamada recursiva en cada mitad
        ordenar(iz)
        ordenar(de)
    
        # Iteradores para recorrer listas
        i = 0
        j = 0
        k = 0

        while i < len(iz) and j < len(de):
            if iz[i] < de[j]:
                lista[k] = iz[i]
                i += 1
            else:
                lista[k] = de[j]
                j += 1
            
            k += 1

        while i < len(iz):
            lista[k] = iz[i]
            i += 1
            k += 1
        
        while j < len(de):
            lista[k] = de[j]
            j += 1
            k += 1

        print(f'iz {iz}, de {de}')
        print(lista)
        print('-')

    return lista



if __name__ == "__main__":
    n = int(input('Cuantos elementos tiene la lista?  '))
    lista = [random.randint(0, 100) for i in range(n)]
    ordenada = ordenar(lista)
    print(ordenada)