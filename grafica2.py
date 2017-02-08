import numpy as np
import pylab as pl

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

#*****************************************************************************
pl.subplot(241)

pl.plot(X, Y + 1, color='blue', alpha=1.00)
pl.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

pl.plot(X, Y - 1, color='blue', alpha=1.00)
pl.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
pl.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red', alpha=.5)

pl.xlim(-np.pi, np.pi)
pl.xticks(())  # borra tincks
pl.ylim(-2.5, 2.5)
pl.yticks(())
pl.title('Grafico Regular')

#*****************************************************************************
pl.subplot(242)

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # arctan(y/x)
# T = np.random.rand(n)


pl.scatter(X, Y, s=50, c=T, alpha=.5)
# pl.scatter(x, y, s=area, c=colors, alpha=0.5)

pl.xlim(-1.5, 1.5)
pl.xticks(())
pl.ylim(-1.5, 1.5)
pl.yticks(())
pl.title('Grafico Dispersion')

#*****************************************************************************
pl.subplot(243)

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

pl.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
pl.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# numeros sobre las barras
for x, y in zip(X, Y1):
    pl.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom', size=6)

for x, y in zip(X, Y2):
    pl.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top', size=6)

pl.xlim(-.5, n)
pl.xticks(())
pl.ylim(-1.25, 1.25)
pl.yticks(())
pl.title('Grafico Barras')

#*****************************************************************************
pl.subplot(2, 4, 4)


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='bone')
# cmap=pl.cm.hot,cmap=pl.cm.hot_r,cmap=pl.cm.cool, cmap='bone'
# el 8 da la cantidad de sub niveles
C = pl.contour(X, Y, f(X, Y), 8, colors='gray', linewidth=.5)
# lineas de contorno
pl.clabel(C, inline=1, fontsize=10, colors='black')
# etiqueta sobre la linea

pl.xticks(())
pl.yticks(())
pl.title('Grafico Contorno')
#*****************************************************************************
pl.subplot(245)


def g(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

n = 20
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = g(X, Y)

pl.imshow(Z, interpolation='nearest', origin='lower')
pl.colorbar(shrink=.7)

pl.xticks(())
pl.yticks(())
pl.title('Grafico Imshow')

#*****************************************************************************
pl.subplot(246)
n = 20
Z = np.ones(n)
Z[-1] *= 2

pl.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)])
# explode da la separacion de las tajadas
pl.axis('equal')
pl.xticks(())
pl.yticks()
pl.title('Grafico Circular')
#*****************************************************************************
pl.subplot(247)

n = 6  # numero de flechas n^2
X, Y = np.mgrid[0:n, 0:n]
T = np.arctan2(Y - n / 2., X - n / 2.)
R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
U, V = R * np.cos(T), R * np.sin(T)

pl.quiver(X, Y, U, V, R, alpha=.5)
# flechas de color , la pos de R da como varia el color de las flechas
pl.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)
# bordes de flecha

pl.xlim(-1, n)
pl.xticks(())
pl.ylim(-1, n)
pl.yticks(())
pl.title('Grafico Campo')

#*****************************************************************************
pl.subplot(248, polar=True)

# ax = pl.axes([0.025, 0.025, 0.95, 0.95], polar=True)

N = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = pl.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(pl.cm.jet(r / 10.))
    bar.set_alpha(0.5)

pl.title('Grafico Polar')

#*****************************************************************************

pl.suptitle(r"$GRAFICAS$", size=30)
pl.show()