from caminante import CaminanteTradicional
from coordenadas import Coordenada
from campo import Campo

import matplotlib.pyplot as plt
from numpy import mean

def graficar(pasos, tipo_caminante, count):
    caminante = tipo_caminante(nombre='Toto')
    origen = Coordenada(0, 0)
    campo = Campo()
    campo.agregar_caminante(caminante, origen)

    plt.subplot(2,2,count)
    plt.title(f'{pasos} pasos')
    plt.grid(True)

    p2 = campo.obtener_coordenada(caminante).posicion()

    for _ in range(pasos):
        p1 = campo.obtener_coordenada(caminante).posicion()
        campo.mover_caminante(caminante)
        p2 = campo.obtener_coordenada(caminante).posicion()
        # print(f'{pasos} pasos. Punto {_}. {p1} {p2}')
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=2.0)

    plt.scatter([0], [0], c="g", linewidth=5.0)
    plt.scatter(p2[0], p2[1], c="r", linewidth=5.0)



def caminata(campo, caminante, pasos):
    inicio = campo.obtener_coordenada(caminante)
    for _ in range(pasos):
        campo.mover_caminante(caminante)

    return inicio.distancia(campo.obtener_coordenada(caminante))


def simular_caminata(pasos, numero_de_intentos, tipo_caminante):
    caminante = tipo_caminante(nombre='Toto')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.agregar_caminante(caminante, origen)
        simular_caminata = caminata(campo, caminante, pasos)
        distancias.append(round(simular_caminata))

    return distancias


def main(distancias_de_caminata, numero_de_intentos, tipo_caminante):
    for count, pasos in enumerate(distancias_de_caminata, 1):
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_caminante)
        distancia_media = mean(distancias)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        print(f'\n{tipo_caminante.__name__} caminó {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

        graficar(pasos, tipo_caminante, count)
    plt.show()


if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, CaminanteTradicional)