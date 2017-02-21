# Ejemplo de transformada de fourier

import pylab as pl
import numpy as np
from numpy import pi
from scipy.fftpack import fft, fftfreq

#************  Creo la senal  ********************

n = 170  # Numero de intervalos
f = 400.0  # Hz
t = np.linspace(0 , 0.04 , n)  # Intervalo de tiempo en segundos
dt = t[1] - t[0]
y = np.sin(2*pi*f*t) - 0.5*np.sin(4*pi*f*t)  # Senal

y2 = y*np.blackman(n)  # Funcion ventana
t = np.linspace(0 , 0.08 , 5*n)
dt = t[1] - t[0]
# Zero-padding
y = np.append(y, np.zeros(4*n))
y2 = np.append(y2, np.zeros(4*n))

escribe = open('funcion.dat', 'w')
for i in range(len(y)):
	dato = str(y[i])
	escribe.write('%s\n' %(dato))
escribe.close()

#*********  Hacemos la transformada  **********************

Y = fft(y)/(5*n)  # Normalizada
Y2 = fft(y2)/(5*n)  # Normalizada
frq = fftfreq(5 * n, dt)  # Recuperamos las frecuencias

#**************  Graficamos  **********************
print(len(y), len(t))
fig = pl.figure(figsize=(6, 8))

ax1 = fig.add_subplot(411)
ax1.plot(t,y)  # Senal pura
pl.ylabel('$y(t)$')
pl.xlim(0, 0.08)
pl.title('Senal Pura')

ax2 = fig.add_subplot(412)
ax2.vlines(frq, 0, abs(Y))  # Espectro de amplitud
pl.ylabel('Abs($Y$)')
pl.xlim(-2000,2000)

ax3 = fig.add_subplot(413)
ax3.plot(t,y2)  # Senal con funcion ventana
pl.ylabel('$y_2(t)$')
pl.xlim(0, 0.08)
pl.title('Senal Filtrada')

ax4 = fig.add_subplot(414)
ax4.vlines(frq , 0 , abs(Y2))  # Espectro de amplitud
pl.xlabel('Frecuencia (Hz)')
pl.ylabel('Abs($Y_2$)')
pl.xlim(-2000,2000)
ax4.annotate(s=u'f = 400 Hz', xy=(400.0, 0.041),
            xytext=(400.0 + 1000.0, 0.02),
            arrowprops=dict(arrowstyle = "->"))
pl.annotate(s=u'f = -400 Hz', xy=(-400.0, 0.041),
            xytext=(-800.0 - 1000.0, 0.02),
            arrowprops=dict(arrowstyle = "->"))
pl.annotate(s=u'f = 800 Hz', xy=(800.0, 0.02),
            xytext=(800.0 + 600.0, 0.01),
            arrowprops=dict(arrowstyle = "->"))
pl.annotate(s=u'f = -800 Hz', xy=(-800.0, 0.02),
            xytext=(-800.0 - 1000.0, 0.01),
            arrowprops=dict(arrowstyle = "->"))

pl.show()