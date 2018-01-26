"""
Armonicos esfericos proyectados sobre la esfera en un mapa de calor.

Ruben E Acosta

2016-02-27
"""
import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors

l = 4    #grado del armónico esférico
m = 2  # orden


# Arrays coordenados para la representación gráfica
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi/2, np.pi/2, 50)
X, Y = np.meshgrid(x, y)

#Arrays de coordenadas esféricas, derivadas de x, y

phi = x.copy()    #copia física
phi[x < 0] = 2 * np.pi + x[x<0]
theta = np.pi/2 - y
PHI, THETA = np.meshgrid(phi, theta)


SH_SP = sp.sph_harm(m, l, PHI, THETA).real    # solo representaremos la parte real

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

xlabels = ['$210^\circ$', '$240^\circ$','$270^\circ$','$300^\circ$','$330^\circ$',
           '$0^\circ$', '$30^\circ$', '$60^\circ$', '$90^\circ$','$120^\circ$', '$150^\circ$']

ylabels = ['$165^\circ$', '$150^\circ$', '$135^\circ$', '$120^\circ$', 
           '$105^\circ$', '$90^\circ$', '$75^\circ$', '$60^\circ$',
           '$45^\circ$','$30^\circ$','$15^\circ$']

fig, ax = plt.subplots(subplot_kw=dict(projection='mollweide'), figsize=(10,8))
im = ax.pcolormesh(X, Y , SH_SP)
ax.set_xticklabels(xlabels, fontsize=16)
ax.set_yticklabels(ylabels, fontsize=16)
ax.set_title('$(Y^4_ 3)$', fontsize=28)
ax.set_xlabel(r'$\boldsymbol \phi$', fontsize=20)
ax.set_ylabel(r'$\boldsymbol{\theta}$', fontsize=20)
ax.grid()
fig.colorbar(im, orientation='horizontal');

