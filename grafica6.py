# graficas de barras

import matplotlib.pyplot as pl
import numpy as np
import datetime as dt

pl.figure('Barras')

#**********************************************************************
pl.subplot(221)

x = np.random.randn(10000)
pl.hist(x, bins = 20, color='y')  # Histograma con 20 intervalos
pl.title('Histograma')

#**********************************************************************
pl.subplot(222)
prima = 600 + np.random.randn(5) * 10  # Valores inventados

# generamos las fechas de los últimos cinco días
fechas = ( dt.date.today() - dt.timedelta(5) ) + dt.timedelta(1) * np.arange(5)

#pl.axes((0.1, 0.3, 0.8, 0.6))  # Definimos la posición de los ejes
pl.bar(np.arange(5), prima, color='g')  # Dibujamos el gráfico de barras
pl.ylim(550,650)  # Range definido [450, 550]
pl.title('Prima de riesgo')
pl.xticks(np.arange(5), fechas, rotation = 15)

print( dt.timedelta(1) , dt.timedelta(2) , dt.timedelta(3) , dt.timedelta(4))

#**********************************************************************
pl.subplot(223)

#pl.axes((0.2,0.1,0.7,0.8))
pl.title(u'Evolución para hoy de los tipos de nubosidad')

# Dibujamos los momentos en que ha habido nubes altas
pl.broken_barh( [(0,1),(3,3), (10,5), (21,3)] , (9500, 1000) )

# Dibujamos los momentos en que ha habido nubes medias
pl.broken_barh([(0,24)], (4500, 1000))

# Dibujamos los momentos en que ha habido nubes bajas
pl.broken_barh([(0,9), (12,5), (20,2)], (1500, 1000))

pl.xlim(-1,25)
pl.yticks([2000, 5000, 10000], ['nubes bajas', 'nubes medias','nubes altas'])
pl.xlabel('t(h)')

#**********************************************************************
pl.subplot(224)

x = np.arange(10) + 1
y = np.random.rand(10)
pl.step(x, y, where = 'mid', color = 'r', linewidth = 3)
pl.title(u"Gráfico escaleras")
pl.xlim(0,11)

pl.show()
