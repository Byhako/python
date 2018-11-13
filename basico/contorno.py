from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np

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

plt.show()


# ////////////////////////////////////////////////////////////
"""
random_state = np.random.RandomState(19680801)

npts = 200
x = random_state.uniform(-2, 2, npts)
y = random_state.uniform(-2, 2, npts)
z = x*np.exp(-x**2 - y**2)
# define grid.

xi, yi = np.mgrid[-2:2:100j, -2:2:200j]
# grid the data.
zi = griddata(x, y, z, xi, yi, interp='linear')
# contour the gridded data, plotting dots at the nonuniform data points.
CS = plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
CS = plt.contourf(xi, yi, zi, 15, vmax=abs(zi).max(), vmin=-abs(zi).max())
plt.colorbar()  # draw colorbar
# plot data points.

plt.show()
"""


"""
plt.pcolormesh(z)
curves = 11.0
m = max([max(row) for row in z])  # max of Z
levels = numpy.linspace(0, m, curves+2)
plt.contour(z, colors="white", levels=levels)
"""