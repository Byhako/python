
#matplotsuperficie.py ilustra un grafico z=f(x,y)=(sin(x))^3cos(y).

import pylab as p
from mpl_toolkits.mplot3d import Axes3D
from numpy import *



print "Tenganga paciencia estoy trabajando"
delta= 0.1

y = arange(-3., 3., delta)
x = arange(-3., 3., delta)
X, Y = p.meshgrid(x,y)
Z = ((sin(X))**3)*cos(Y)

fig = p.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z) 
ax.plot_wireframe(X, Y, Z, color = 'r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

p.show()
