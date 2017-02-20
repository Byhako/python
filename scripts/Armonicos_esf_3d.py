from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

f = np.linspace(0, 2 * np.pi, 100)
t = np.linspace(0, np.pi, 100)

r=np.sqrt(5/16*np.pi)*((3.0*np.cos(t)**2)-1.0)  #armonico esferico

x = np.abs(r) * np.outer(np.cos(f), np.sin(t))
y = np.abs(r) * np.outer(np.sin(f), np.sin(t))
z = np.abs(r) * np.outer(np.ones(np.size(f)), np.cos(t))
ax.plot_surface(x, y, z,  rstride=3, cstride=3,cmap=cm.jet,
        linewidth=0.0001, antialiased=False)

plt.title('Y_20',size=18,color='m') #titulo
plt.xlabel('EJE X') #nombre del eje x
plt.ylabel('EJE Y') #mombre del eje y

plt.show()
"""
Armonicos esfericos en 3D. Para cada uno se debe cambiar la ecuacion 
"""