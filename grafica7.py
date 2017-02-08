# Grafico de colores

import matplotlib.pyplot as pl
import numpy as np

pl.figure('Colores')

#**********************************************************************
pl.subplot(231)

# Definimos un vector con el % de visitas del top ten de paises
visitas = [43.97, 9.70, 7.42, 6.68, 3.91, 3.85, 3.62, 3.43, 3.16, 3.04]

# Un ultimo elemento que recoge el % de visitas de otros paises
visitas = np.append(visitas, 100.0 - np.sum(visitas))

paises = [u'España', u'México', 'Chile', 'Argentina', 'Colombia', 'Ecuador',
					u'Perú', 'USA', 'Islandia', 'Venezuela', 'Otros']

# Esto nos ayudara a destacar algunos quesitos
explode = [0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0.2, 0]

pl.pie(visitas, labels = paises, explode = explode)
pl.title(u'Porcentaje de visitas por país')

#**********************************************************************
pl.subplot(232)

x = np.random.rand(20)
y = np.random.rand(20)
t = np.random.rand(20)*3000

# Pintamos las triangulaciones con contornos de color
pl.tricontourf(x, y, t)

# Pintamos las lineas de contorno en color negro
pl.tricontour(x, y, t, colors = 'k')

# Pintamos la posicion de las estaciones de medida.
pl.scatter(x, y)

"""
Tiangulaciones

matplotlib.tri.triangulation
"""

#**********************************************************************
pl.subplot(233)

# Representa el numero de veces que los valores de dos series (x e y)
# se encuentran en determinado intervalo de datos.

x = np.random.randn(10000)
y = np.random.randn(10000)

# Representamos como estan distribuidos bidimensionalmente con ayuda de hexbin,
# en este caso definimos un tamaño del grid de 20
pl.hexbin(x,y, gridsize = 20)

pl.colorbar()

#**********************************************************************
pl.subplot(234)
# Dibujar una matriz con cuadros de colores en funcion del valor
# de cada uno de los elementos de la matriz

x = np.sort(np.random.randn(30))
y = np.sort(np.random.randn(30))

x = np.arange(-3,3,0.2)
y = np.arange(-3,3,0.2)

# Creamos dos matrices cuadradas
X, Y = np.meshgrid(x, y)

Z = np.sqrt( X**2 + Y**2)
pl.pcolor(Z)  # Representamos la última matriz con matshow,pcolor

# Colocamos líneas de contorno para la matriz
pl.contour(np.arange(30), np.arange(30), Z, 10, colors = 'k')


#**********************************************************************
pl.subplot(235)

lon = np.arange(15) - 10.  # longitudes
lat = np.arange(15) + 30.  # latitudes

lon, lat = np.meshgrid(lon, lat)

# Componentes x,y del vector viento a partir de una lon y una lat determinada
x = np.random.randn(15 * 15)
y = np.random.randn(15 * 15)

#  Definimos una serie de colores para las flechas
colores = ['k','r','b','g','c','y','gray']


pl.title('Flechas de un viento un poco loco')
pl.xlabel('longitud')
pl.ylabel('latitud')
pl.quiver(lon, lat, x, y, color = colores)  # Dibujamos las flechas 'locas'

#**********************************************************************

pl.show()