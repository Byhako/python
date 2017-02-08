from numpy import *
from pylab import *

#****************************
me=9.1094e-31
hbar=1.0546e-34
qe=1.6022e-19
#****************************

X=arange(5,20,0.1)
x=X*1e-9   #ancho del pozo

e1=((hbar*pi)**2/(2*me*x*x))*1000/qe
e2=((hbar*pi)**2/(2*me*x*x))*2000/qe
e3=((hbar*pi)**2/(2*me*x*x))*3000/qe
e4=((hbar*pi)**2/(2*me*x*x))*4000/qe

plot(X,e1,linewidth=1.5)
plot(X,e2,linewidth=1.5)
plot(X,e3,linewidth=1.5)
plot(X,e4,linewidth=1.5)
axis([5.0,20.0,-0.2,20])#ejes de una grafica
xlabel('Longitud(nm)') #nombre del eje x
ylabel('Energia(mEv)') #mombre del eje y
title('Energia Vs. Ancho',color='m',size=18) #titulo
grid(True) #rectangulos grises
legend(('n=1','n=2','n=3','n=4',), loc=0)

show()