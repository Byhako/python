from numpy import *
from pylab import *

#****************************
me=9.1094e-31
hbar=1.0546e-34
qe=1.6022e-19
#****************************

x=20e-9   #ancho del pozo

E=[]
energia=((hbar*pi)**2/(2*me*x*x))*1000/qe

for i in range(5):
    n=i+1
    en=energia*n*n
    E.append(en)
    
u=arange(0,24,4)

for i in range(5):
    v=[]
    for j in range(6):
        d=E[i]
        v.append(d)
    plot(u,v,linewidth=2)  
    
xlabel('Longitud(nm)',size=14) #nombre del eje x
ylabel('Energia(mEv)',size=14) #mombre del eje y
title('Niveles de Energia',color='r',size=18) #titulo
legend(('E(n=1)','E(n=2)','E(n=3)','E(n=4)','E(n=5)',), loc=0)       
show()    