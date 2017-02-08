"""
Make a histogram of normally distributed random numbers and plot the
analytic PDF over it.

Ruben E Acosta.

2016-02-27
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import timeit

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)   #  vector de pasos aleatorios

fig = plt.figure()
ax = fig.add_subplot(111)

# histograma
n, bins, patches = ax.hist(x, 50, normed=1, facecolor='blue', alpha=0.75)

# hist uses np.histogram under the hood to create 'n' and 'bins'.
# np.histogram returns the bin edges, so there will be 50 probability
# density values in n, 51 bin edges in bins and 50 patches.  To get
# everything lined up, we'll compute the bin centers
bincenters = 0.5*(bins[1:]+bins[:-1])

# Ajuste gausiano
y = mlab.normpdf( bincenters, mu, sigma)
l = ax.plot(bincenters, y, 'r', linewidth=2)

ax.set_xlabel('Pasos')
ax.set_ylabel('Probabilidad')
ax.set_title(r'Caminos Aleatorios')
ax.set_xlim(40, 160)  #intervalo eje x
ax.set_ylim(0, 0.03)  #intervalo eje y
ax.grid(True)   #malla
tiempo=t.timeit()  
print(tiempo)
plt.show()
