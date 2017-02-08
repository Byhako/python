# Tipos de grafico
import matplotlib.pyplot as pl
import numpy as np

##
pl.subplot(231)
x = np.arange(100)
y = np.random.rand(100)
pl.plot(x,y, color = 'black', label = 'x, f(x)')
pl.plot(x[y > 0.9], y[y > 0.9], 'bo', label = 'f(x) > 0.9')
pl.axhspan(0.9, 1, alpha = 0.1)  # banda de color
pl.ylim(0,1.5)
pl.legend()
pl.title(u'Representacion de (x, f(x))')
pl.xlabel('valores x')
pl.ylabel('valores f(x)')

## pl.stem(). Dibuja lineas verticales desde una linea base
pl.subplot(232)
x = np.arange(25) + 1
y = np.random.rand(25) * 10.

y_norm = (y - y.mean()) / y.std() # normalizamos

pl.xlim(np.min(x) - 1, np.max(x) + 1)
pl.ylim(np.min(y_norm)-1, np.max(y_norm)+1)

pl.stem(x[y_norm > 0],y_norm[y_norm > 0], linefmt='k-.',
         markerfmt='go', basefmt='b-')  # valores por encima
pl.stem(x[y_norm < 0],y_norm[y_norm < 0], linefmt='k-.',
         markerfmt='ro', basefmt='b-')  # valores por debajo

pl.title(u'Representacion de (x, f(x))')
pl.xlabel('valores x')
pl.ylabel('valores f(x)')

##   pl.fill_betweenx()
pl.subplot(233)
x = np.arange(25) + 1
y1 = np.random.rand(25) * 10.
y2 = np.random.rand(25) * 10.
pl.xlim(np.min(x) - 1, np.max(x) + 1)
pl.ylim(np.min([y1, y2])-1, np.max([y1, y2])+1)
pl.plot(x, y1, 'k-', linewidth = 2, label = 'Serie 1')
pl.plot(x, y2, 'k-.', linewidth = 2, label = 'Serie 2')

pl.fill_between(x, y1, y2, where = (y1 < y2), color = 'g', interpolate = True)  # Pinta color verde entre las líneas cuando y1 < y2

pl.fill_between(x, y1, y2, where = (y1 > y2), color = 'r', interpolate = True)  # Pinta color rojo entre las líneas cuando y1 > y2

pl.legend()
pl.title('Ejemplo de pl.fill_between()')
pl.xlabel('valores x')
pl.ylabel('valores y')

## otro ejemplo de pl.fill
pl.subplot(234)
s1x = [0.3,0.3,0.7,0.7,0.5,0.5,1,1,0.7,0.7]
s1y = [0.5,1.4,1.4,1.5,1.5,1.9,1.9,1.1,1.1,0.5]
o1x = [0.6,0.6,0.7,0.7]
o1y = [1.7,1.8,1.8,1.7]
s2x = [0.8,0.8,1.1,1.1,1.5,1.5,1.1,1.1,1.3,1.3]
s2y = [0.2,1,1,1.6,1.6,0.7,0.7,0.6,0.6,0.2]
o2x = [1.1,1.1,1.2,1.2]
o2y = [0.3,0.4,0.4,0.3]
pl.fill(s1x, s1y, color = 'b')
pl.fill(o1x,o1y, color = 'w')
pl.fill(s2x, s2y, color = 'g')
pl.fill(o2x,o2y, color = 'w')
pl.title(u'Símbolo de python cutre')
pl.ylim(0.1,2)

## diagrama de caja-bigote
pl.subplot(235)

# Creamos unos valores para la altura de 100 espanolas
alt_esp = np.random.randn(100)+165 + np.random.randn(100) * 10
# Creamos unos valores para la altura de 100 alemanas
alt_ale = np.random.randn(100)+172 + np.random.randn(100) * 12
# Creamos unos valores para la altura de 100 tailandesas
alt_tai = np.random.randn(100)+159 + np.random.randn(100) * 9

# El valor por defecto para los bigotes es 1.5*IQR pero lo escribimos explicitamente
pl.boxplot([alt_esp, alt_ale, alt_tai], sym = 'ko', whis = 1.5)

pl.xticks([1,2,3], ['Esp', 'Ale', 'Tai'], size = 'small', color = 'k')
pl.ylabel(u'Altura (cm)')


pl.show()

