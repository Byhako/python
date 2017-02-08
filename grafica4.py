# ejemplos de uso de axes, dos ejes, polar, enfasis.

import sys

import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import math

pl.figure("Axes",figsize = (5,5))
pl.plot(np.exp(np.linspace(0,10,100)))  # Dibuja una exponencial de 0 a 10
pl.axes([0.2,0.55,0.3,0.3], axisbg = 'gray')
pl.plot(np.sin(np.linspace(0,10,100)), 'b-o', linewidth = 2)


#******************************************************************************

#print('Version de Python usada: ', sys.version)
#print('Version de Numpy usada: ', np.__version__)
#print('Version de Matplotlib usada: \n', matplotlib.__version__)

## Creamos un conjunto de datos
datos = np.arange(10,90,10)
## Los datos los queremos en tanto por ciento
datos = datos * 100. / datos.sum()
## Direcciones en radianes empezando por el N
## A las direcciones les restamos 22.5 para que las barras
## esten centradas exactamente en 0, 45, 90,...
direcciones = (np.arange(0, 360, 45) - 22.5) * math.pi / 180.
sectores = ['N','NE','E','SE','S','SW','W','NW']

fig = pl.figure('Polar',figsize = (5,5))
ax = fig.add_subplot(111, polar=True)
## La siguiente linea de codigo hace que los datos vayan en el
## sentido de las agujas del reloj
ax.set_theta_direction(-1)
## La siguiente linea coloca el 'origen' de la rotacion
## donde le indiquemos, en este caso en Norte.
ax.set_theta_zero_location('N')
## Titulo
ax.set_title('Procedencia de las nubes en agosto (%)\n')
## Dibujamos los datos
ax.bar(direcciones, datos)
## Colocamos las etiquetas del eje x
ax.set_thetagrids(np.arange(0, 360, 45), sectores, frac = 1.1, fontsize = 14)

#******************************************************************************

pl.figure('Dos ejes',figsize = (5,5))
pl.plot(np.arange(100), 'b')  # Dibujamos una linea recta azul
pl.xlabel('Valores de x')  # Ponemos etiqueta al eje x
pl.ylabel(u'Linea azul')  # Ponemos etiqueta al eje y
pl.twinx()  # Creamos un segundo eje y
pl.plot(np.exp(np.linspace(0,5,100)), 'g')  #exponencial con y en segundo eje
pl.ylabel(u'Linea verde')  # Ponemos etiqueta al segundo eje y
pl.xlim(-10,110)

#******************************************************************************

pl.figure('Enfasis',figsize = (5,5))

pl.scatter(np.random.randn(1000), np.random.randn(1000))  # scatterplot
pl.axvline(-0.5, color = 'g')  # linea vertical verde en x = -0.5
pl.axvline(-0.5, color = 'g')  # linea vertical verde en x = 0.5
pl.axhline(-0.5, color = 'g')  # linea horizontal verde en x = -0.5
pl.axhline(-0.5, color = 'g')  # linea horizontal verde en x = 0.5
pl.axvspan(-0.5,0.5, alpha = 0.25)  #recuadro vertical con transparencia 0.25
pl.axhspan(-0.5,0.5, alpha = 0.25)  #recuadro horizontal entre x[-0.5,0.5]

pl.show()

"""
pl.axes([x,y,a,b])

x,y = coordenadas de la esquina inferior izquierda del grafico
a,b = ancho y alto del grafico.

pl.xscale()
pl.semilogy()

"""