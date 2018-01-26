"""
Usando la ecuacion polar, grafico la conica.
Tambien la puedo rotar.

Ruben E Acosta.

2016-02-27
"""

import numpy as np
import matplotlib.pyplot as plt
import time
ini=time.time()
# r = p / (1 + e cos f)

#=================================================================
def conica(p,e):
    fmax = np.arccos(-1/e) #maximo de la anomalia verdadera
    
    if e<1: 
        f = np.linspace(-np.pi,np.pi,1000)
    elif e>1:
        f = np.linspace(-0.8*fmax,0.8*fmax,1000)    
    else:
        f = np.linspace(-0.8*np.pi,0.8*np.pi,1000)
    
    rs = p/(1 + e*np.cos(f))  #radio vector
    xs = rs*np.cos(f)
    ys = rs*np.sin(f)
    
    #para hiperbola, desplazo, y obtengo 2da rama.
    if e>1:
        h = np.min(rs) + np.abs(p/(1-e*e)) #desplazamiento
        x2=[]
        y2=[]
        for i in range(len(xs)):     #desplazo
            x2.append(xs[i]-h)        
        for i in range(len(xs)):     #seguna rama
            x2.append(-1*(xs[i]-h))
            
        for i in range(len(ys)):
            y2.append(ys[i])  
        for i in range(len(ys)):
            y2.append(ys[i])      
    xs=x2
    ys=y2  
    sol = [xs,ys]
    return sol
#=================================================================

# Grafica
def graf(x,y):
    ext = 1.1*max(max(np.abs(x)),max(np.abs(y)))
    xx = np.arange(-ext,ext+1,1)
    yy = xx - xx

    plt.figure(figsize = (6,6))
    plt.plot(xx,yy,'k')
    plt.plot(yy,xx,'k')
    plt.plot(x,y,'.')
    plt.title('Ecuacion Polar')
    plt.xlim(-ext,ext)
    plt.ylim(-ext,ext)
    plt.grid()
    plt.show()
    return 
#=================================================================    

def rot(x,y,angulo):
    #matriz de rotacion
    t=np.radians(angulo)
    sint = np.sin(t)
    cost = np.cos(t)

    Mrot = np.array([[cost,-sint],[sint,cost]])

    xps = []
    yps = []
    for x1,y1 in zip(x,y):
        r = [x1,y1]
        rp = Mrot.dot(r)
        xps += [rp[0]]
        yps += [rp[1]]
    
    sol = [xps,yps]
    return sol 
#=================================================================    

# Matriz de Rotacion 3D
def rot3d(t,axis):
    R=np.identity(3)
    r=np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]])
    
    if axis=='z':
        R[0:2,0:2] = r
    elif axis=='x':
        R[1:3,1:3] = r
    else:
        R[0,0] = r[0,0]; R[0,2] = r[0,1]
        R[2,0] = r[1,0]; R[2,2] = r[1,1]
    
    return R
    
#=================================================================
    
#Parametros de entrada
#********************************
p = 2     # semi-latus rectum    
e = 1.5   # excentricidad
angulo = 30

#********************************

x,y = conica(p,e)          #creo 
x1,y1 = rot(x,y,angulo)    #roto 
graf(x1,y1)                #grafico