from numpy import *
from pylab import *

L=20

x=arange(0,L+0.1,0.1)
f1=(sqrt(2/L)*sin((pi*1*x)/L))**2
f2=(sqrt(2/L)*sin((pi*2*x)/L))**2
f3=(sqrt(2/L)*sin((pi*3*x)/L))**2
f4=(sqrt(2/L)*sin((pi*4*x)/L))**2

subplot(221)
plot(x,f1,linewidth=1.5)
xlabel('Longitud(nm)',size=14) #nombre del eje x
ylabel('Probabilidad',size=14) #mombre del eje y
#title('Funcion de Onda',color='r',size=18) #titulo
legend(('n=1',), loc=0)

subplot(222)
plot(x,f2,linewidth=1.5)
xlabel('Longitud(nm)',size=14) #nombre del eje x
ylabel('Probabilidad',size=14) #mombre del eje y
#title('Funcion de Onda',color='r',size=18) #titulo
legend(('n=2',), loc=0)

subplot(223)
plot(x,f3,linewidth=1.5)
xlabel('Longitud(nm)',size=14) #nombre del eje x
ylabel('Probabilidad',size=14) #mombre del eje y
#title('Funcion de Onda',color='r',size=18) #titulo
legend(('n=3',), loc=0)

subplot(224)
plot(x,f4,linewidth=1.5)
xlabel('Longitud(nm)',size=14) #nombre del eje x
ylabel('Probabilidad',size=14) #mombre del eje y
#title('Funcion de Onda',color='r',size=18) #titulo
legend(('n=4',), loc=0)

# plot(x,f1,linewidth=1.5)
# plot(x,f2,linewidth=1.5)
# plot(x,f3,linewidth=1.5)
# plot(x,f4,linewidth=1.5)
# 
# u=arange(0,25,5)
# v2=[1,1,1,1,1]
# v3=[2,2,2,2,2]
# v4=[3,3,3,3,3]
# 
# plot(u,v2,'k')
# plot(u,v3,'k')
# plot(u,v4,'k')
# 
# xlabel('Longitud(nm)',size=14) #nombre del eje x
# ylabel('Energia',size=14) #mombre del eje y
# title('Funciones de Onda',color='m',size=18) #titulo
# legend(('n=1','n=2','n=3','n=4',), loc=0)

show()