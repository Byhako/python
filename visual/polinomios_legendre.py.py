#GRAFICA POLINOMIOS DE LEGENDRE

from math import *
from visual.graph import * #para poder graficar
graph = gdisplay(x=0,y=0,width=500,height=500,title="polinomios de Legendre",xmax=1.0,xmin=-1.0,ymax=1.0,ymin=-1.0)
polinomio = gcurve()

n = 101 #los puntos para graficar
pnp = zeros((n),float) #nuestro pnp sera Pm+1(x). Reservamos 101 posiciones de memoria de punto flotante. Para el polinomio m+1
pn = zeros ((n),float) #para el polinomio m
pnm = zeros((n),float) #para polinomio m-1

def p0():
    x = -1
    dx = 0.02
    for i in range(0,n):
        pnm[i]=1.0
        polinomio.plot(pos = (x,pnm[i]))
        x = x+dx
def p1():
    x = -1.0 #empezar
    dx = 0.02 #incremento en x
    for i in range(0,n):
        pn[i]= x
        polinomio.plot(pos = (x,pn[i]))
        x = x+dx #x = x+dx
def pnext():
    for m in range(1,7): #para todos los polinomios
        x = -1.0 #comienzo
        dx = 0.02 #incremento x
        for i in range(0,n):
            pnp[i] = (2*m+1)*x*pn[i]/(m+1)-m*pnm[i]/(m+1) #Recurrencia
            polinomio.plot(pos = (x,pnp[i])) #grafica pnp
            x = x+dx
        for i in range(0,n):
            pnm[i] = pn [i]
            pn[i] = pnp [i]

p0()
p1()
pnext()
                        
            
                       
            
