from pylab import *
#grafico los 7 primeros polinomios de Laguerre.
x=arange(-1,5.5,0.1)


y1=1+x-x
y2=-1*x+1
y3=(1/2)*(x*x-4*x+2)
y4=(1/6)*(-x*x*x+9*x*x-18*x+6)
y5=(1/24)*(x**4-16*x**3+7*x*x-96*x+24)
y6=(1/120)*(-x**5+25*x**4-200*x**3+600*x*x-600*x+120)
y7=(1/720)*(x**6-36*x**5+450*x**4-2400*x**3+5400*x*x-4320*x+720)

plot(x,y1,'r')
plot(x,y2,'b')
plot(x,y3,'k')
plot(x,y4,'g')
plot(x,y5,'c')
plot(x,y6,'m')
plot(x,y7,'y')

axis([-1.0,5.0,-1.0,2.0])#ejes de una grafica
xlabel('EJE X') #nombre del eje x
ylabel('EJE Y') #mombre del eje y
title('Polinomy Laguerre',color='m') #titulo
grid(True) #rectangulos grises
legend(('n=0','n=1','n=2','n=3','n=4','n=5','n=6',), loc=0)#no olvides la coma al final de seno

show()