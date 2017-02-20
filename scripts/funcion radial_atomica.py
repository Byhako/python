from pylab import *
from numpy import *
import time
inicio=time.time()
##**************************************
eps0=1.0/(4*pi)    #a.u
hbar = 1.0         #a.u
me=1.0             #a.u
mu=1.0             #a.u
q=1.0              #a.u
##**************************************

au=(4*pi*eps0*hbar*hbar)/(mu*q*q)

r1=arange(0.1,5,0.01)
c1=0.0*r1
R1=2.0*((1.0/au)**(3.0/2.0))*exp(-r1/au)
d1=r1*r1*R1*R1

r2=arange(0.1,12,0.01)
c2=0.0*r2
R2=2.0*(0.5**(3.0/2.0))*(1-r2/2)*exp(-r2/2.0)
d2=r2*r2*R2*R2
R3=(1.0/sqrt(3.0))*(0.5**(3.0/2.0))*(r2)*exp(-r2/2.0)
d3=r2*r2*R3*R3

r3=arange(0.1,18,0.01)
c3=0.0*r3
R4=2.0*((1.0/3.0)**(3.0/2.0))*(1.0-2.0*r3/3.0+2.0*r3*r3/27)*exp(-r3/3.0)
d4=r3*r3*R4*R4
R5=(4.0*sqrt(2)/9.0)*(1.0-r3/6.0)*(r3)*((1.0/3.0)**(3.0/2.0))*exp(-r3/3.0)
d5=r3*r3*R5*R5
R6=(4.0/(27*sqrt(10)))*((1.0/3.0)**(3.0/2.0))*(r3*r3)*exp(-r3/3.0)
d6=r3*r3*R6*R6

##**************************************
subplot(6,2,1)
plot(r1,R1)
plot(r1,c1,'k')
ylabel('$R_{10}$',size=12) 
xlabel('r')
xticks( arange(6) ,size=8)
yticks( arange(0.0,3.0,1.0) ,size=8)
title('$\mathit{Radial Functions}$',color='r',size=16)

subplot(6,2,2)
plot(r1,d1)
ylabel('$(rR_{10})^2$', size=12) 
xlabel('r')
yticks( arange(0.0,0.8,0.2),size=8 )
xticks(size=8)
title('$\mathit{Distrubution Functions}$',color='r',size=16)


subplot(6,2,3)
plot(r2,R2)
plot(r2,c2,'k')
ylabel('$R_{20}$',size=12) 
xlabel('r')
yticks( arange(-0.2,0.8,0.2),size=8 )
xticks(arange(0,14,2),size=8)

subplot(6,2,4)
plot(r2,d2)
ylabel('$(rR_{20})^2$', size=12) 
xlabel('r')
yticks( arange(0.0,0.22,0.07),size=8 )
xticks(arange(0,14,2),size=8)

subplot(6,2,5)
plot(r2,R3)
plot(r2,c2,'k')
ylabel('$R_{21}$',size=12) 
xlabel('r')
yticks( arange(0.0,0.18,0.04) ,size=8)
xticks(size=8)

subplot(6,2,6)
plot(r2,d3)
ylabel('$(rR_{21})^2$', size=12) 
xlabel('r')
yticks( arange(0.0,0.3,0.1) ,size=8)
xticks(size=8)

subplot(6,2,7)
plot(r3,R4)
plot(r3,c3,'k')
ylabel('$R_{30}$',size=12)  
xlabel('r')
yticks( arange(-0.1,0.4,0.1) ,size=8)
xticks(arange(0,20,3),size=8)

subplot(6,2,8)
plot(r3,d4)
ylabel('$(rR_{30})^2$', size=12)
xlabel('r')
yticks( arange(0.0,0.16,0.04) ,size=8)
xticks(arange(0,20,3),size=8)

subplot(6,2,9)
plot(r3,R5)
plot(r3,c3,'k')
ylabel('$R_{31}$',size=12)  
xlabel('r')
yticks( arange(-0.04,0.16,0.04),size=8 )
xticks(arange(0,20,3),size=8)

subplot(6,2,10)
plot(r3,d5)
ylabel('$(rR_{31})^2$', size=12) 
xlabel('r')
yticks( arange(0.0,0.16,0.04),size=8 )
xticks(arange(0,20,3),size=8)

subplot(6,2,11)
plot(r3,R6)
plot(r3,c3,'k')
ylabel('$R_{32}$',size=12)  
xlabel('$r$',size=14,weight='bold')
yticks( arange(0.0,0.08,0.02) ,size=8)
xticks(arange(0,20,3),size=8)

subplot(6,2,12)
plot(r3,d6)
ylabel('$(rR_{32})^2$', size=12)
xlabel('$r$',size=14,weight='heavy')
yticks( arange(0,0.16,0.04) ,size=8)
xticks(arange(0,20,3),size=8)

show()
##**************************************


fin=time.time()
print('Tiempo de ejecucion: %6f' %(fin-inicio))
"""
Para el atomo de hidrogeno, para la parte radial, se grafica 
para n=1,2,3 la parte radial de la solucion a la ecuacion de
onda, y la distribucion radial.  Bransden 3.3
"""