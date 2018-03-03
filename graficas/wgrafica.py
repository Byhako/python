import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 2, 100)

y = x**3 + 2*x*x - 6


plt.plot(x, y, color="blue", linewidth=2.0, linestyle='-',label="cosine")

# Establecer limites
plt.xlim(x.min() * 0.9, x.max() * 1.1)
plt.ylim(y.min() * 0.9, y.max() * 1.1)

## Moviendo los ejes al centro

ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior
ax.xaxis.set_ticks_position('bottom')  #mueve rayitas
ax.spines['bottom'].set_position(('data',0)) #mueve eje x
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',1)) # mueve eje y

## Mejorando las etiquetas

# fondo blancusco semi-transparente para las etiquetas
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.6))

## Ticks
#pl.xticks([],[])
#pl.yticks([],[])
#pl.legend(loc=0)

plt.show()