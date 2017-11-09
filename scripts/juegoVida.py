# coding: utf-8

"""Juego de la vida de Conway.
Autor: Juan Luis Cano <juanlu001@gmail.com>
El tablero es un array de NumPy, donde 0 significa célula muerta y 1 célula
viva. Se muestra una animación con matplotlib.
"""

from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation


def vecindario(b):
    """Array de células vivas en el vecindario."""
    vecindario = (
        np.roll(np.roll(b, 1, 1), 1, 0) +  # Abajo-derecha
        np.roll(b, 1, 0) +  # Abajo
        np.roll(np.roll(b, -1, 1), 1, 0) +  # Abajo-izquierda
        np.roll(b, -1, 1) +  # Izquierda
        np.roll(np.roll(b, -1, 1), -1, 0) +  # Arriba-izquierda
        np.roll(b, -1, 0) +  # Arriba
        np.roll(np.roll(b, 1, 1), -1, 0) +  # Arriba-derecha
        np.roll(b, 1, 1)  # Derecha
    )
    return vecindario


def paso(b):
    """Paso en el juego de la vida de Conway."""
    v = vecindario(b)
    buffer_b = b.copy()  # Hacemos una copia de la matriz
    for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if v[i, j] == 3 or (v[i, j] == 2 and buffer_b[i, j]):
                buffer_b[i, j] = 1
            else:
                buffer_b[i, j] = 0
    return buffer_b


# Parámetros del problema
GENERACIONES = 50
N = 32*2
M = 16*3*2

# Construimos el tablero
tablero = np.zeros((N, M,3))

# Añadimos una nave
tablero[1, 1:4, 1] = 1
tablero[2, 1, 1] = 1
tablero[3, 2, 1] = 1

fig = plt.figure(figsize=(8, 12), dpi=80)
plt.axis('off')

b = tablero[:,:,1]
#plt.imshow(tablero,  cmap=cm.gray_r)
#plt.savefig('uno.png')
#plt.show()


for i in range(10):
    fig = plt.figure(figsize=(4, 4), dpi=80)
    plt.axis('off')
    b = paso(b)
    plt.grid(True)
    tablero[:,:,1] = b
    imagen = plt.imshow(tablero,  cmap=cm.gray_r)





