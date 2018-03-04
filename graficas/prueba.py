from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
from paleta import *

# Data to plot.
x, y = np.meshgrid(np.arange(0,10.1,0.1), np.arange(0,10.1,0.1))
z = np.sin(0.5 * x) * np.cos(0.52 * y)

cmap = plt.cm.viridis # viridis hot rainbow
orientation = 'vertical'   # horizontal,  vertical
leveLines = [round(i,1) for i in np.linspace(-1,1,10) ]
leveColor = [round(i,1) for i in np.linspace(-1,1,10) ]

cs = plt.contour(x,y,z,leveLines, colors='k', linewidths=0.5 ) # lineas de contorno
plt.clabel(cs, fmt='%2.1f', colors='w', fontsize=10) # label sobre lineas
cs = plt.contourf(x,y,z,leveColor,cmap=cmap)  # coloreo contorno
cb = plt.colorbar(orientation=orientation,)  # draw colorbar
cb.set_label('Some Units')
plt.grid(c='k', ls='-', alpha=0.3)

plt.xlabel('Eje x', size=18)
plt.ylabel('Eje y', size=18)
plt.title('Contorno', size=20)

plt.xticks(np.arange(0,12,2),np.arange(0,12,2),size=12)
plt.yticks(np.arange(2,12,2),np.arange(2,12,2),size=12)

print(len(leveColor))
miscolores = Colores(cmap, leveColor)
print (miscolores)

plt.show()
