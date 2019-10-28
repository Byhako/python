# Vuelos con busqueda con profundidad iterativa
from arbol import Nodo

def bus_prof_iter(nodo, solucion):
    for limite in range(1, 2):
        visitados = []
        sol = busqueda_recursiva(nodo, solucion, visitados, limite)
        if sol != None:
            return sol

def busqueda_recursiva(nodo, solucion, visitados, limite):
    nodo_visitado = nodo.get_datos()
    visitados.append(nodo_visitado)
    if nodo.get_datos() == solucion:
        return nodo
    else:
        # Expandir nodos hijo
        dato_nodo = nodo.get_datos()
        lista_hijos = []
        for un_hijo in conexiones[dato_nodo]:
            hijo = Nodo(un_hijo)
            if not hijo.get_datos() in visitados:
                lista_hijos.append(hijo)

        nodo.set_hijos(lista_hijos)

        for nodo_hijo in nodo.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                # llamada recursiva
                sol = busqueda_recursiva(nodo_hijo, solucion, visitados, limite)
                if sol != None:
                    return sol

    return None

if __name__ == "__main__":
    conexiones = {
        'Malaga': ['Salamanca', 'Madrid', 'Barcelona'],
        'Sevilla': ['Santiago', 'Madrid'],
        'Granada': ['Valencia'],
        'Valencia': ['Barcelona'],
        'Madrid': ['Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander'],
        'Salamanca': ['Malaga', 'Madrid'],
        'Santiago': ['Sevilla', 'Santander', 'Barcelona'],
        'Santander': ['Santiago', 'Madrid'],
        'Zaragoza': ['Barcelona'],
        'Barcelona': ['Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia']
    }

    estado_inicial = 'Malaga'
    solucion = 'Santiago'
    nodo_inicial = Nodo(estado_inicial)
    nodo = bus_prof_iter(nodo_inicial, solucion)

    if nodo != None:
        resultado = []
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print('Solucion no encontrada. :(')
