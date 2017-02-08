"""
Usando el semi latus rectum, la excentricidad y el angulo de inclinacion, 
calulo ecuacion algebraica, imprimo los coeficientes,el discriminante y realizo la grafica.

Ruben E Acosta.

2016-02-27
"""

import numpy as np
import pylab as plt 
import time
ini=time.time()

#=================================================================
def conica(p,e,angulo):
    """
    Funcion que calcula los coeficientes de la ecuacion carteciana
    general, discriminante y vectores xs, ys para graficar la conica.
    
    p=semi latus.rectum
    e=excentricidad
    angulo= grados
    """
    if e!=1.0:
        a=p/(1-e*e)          # semi eje mayor
        c=a*e                # focos
        h=-c 
                        # desplazamiento en x
    if e<1.0: #elipse
        b=np.sqrt(a*a-c*c)   # semi eje menor
        A1 = b**2
        C1 = a**2
        D1 = -2*h*b*b
        E1 = 0.0
        F1 = b*b*h*h - a*a*b*b
    elif e>1.0:  #hiperbola
        b=np.sqrt(c*c-a*a)   # semi eje menor
        A1 = b**2
        C1 = -a**2
        D1 = 0.0
        E1 = 0.0
        F1 = - a*a*b*b   
    else:    
        A1 = 0.0
        C1 = -1.0
        D1 = 4.0*p
        E1 = 0.0
        F1 = 0.0


    #coeficientes ecuacion algebraica
    

    #coeficientes rotados

    t=np.radians(angulo)
    ct=np.cos(t)
    st=np.sin(t)
    tt=np.tan(2*t)

    M1 = np.matrix([[ct**2,st*ct,st**2],[st**2,-st*ct,ct**2],[tt,-1,-tt]])
    v1 = np.matrix([[A1],[C1],[0]])
    R1 = M1.getI()*v1

    M2 = np.matrix([[ct,st],[-st,ct]])
    v2 = np.matrix([[D1],[E1]])
    R2 = M2.getI()*v2

    A = float(R1[0])
    B = float(R1[1])
    C = float(R1[2])
    D = float(R2[0])
    E = float(R2[1])
    F = float(F1)

    # Matriz de Coeficientes
    print(t,A1,C1)
    Cmat = np.matrix([[A,B/2,D/2],[B/2,C,E/2],[D/2,E/2,F]])

    # Signo de la matriz

    det = np.linalg.det(Cmat)

    eta=1.0
    if det>0: eta=-1.0

    # Discriminante

    dis = B**2 - 4*A*C

    # Construyo vectores 

    xs = []
    ys = []

    for x in np.arange(-100,100,0.05):
    
        coeficientes=[C,E+B*x,A*x**2+D*x+F]
        raices=np.roots(coeficientes)

        for y in raices:

            if np.abs(y.imag)<1.0e-5:

                xs.append(x)
                ys.append(y)

    sol=[dis,A,B,C,D,E,F,xs,ys]
    return sol     
#=================================================================
# Gráfica
def graf(x,y):
    ext=1.1*max(max(np.abs(x)),max(np.abs(y)))
    xx=np.arange(-ext,ext+1,1)
    yy=xx-xx

    plt.figure(figsize=(6,6))
    plt.plot(xx,yy,'k')
    plt.plot(yy,xx,'k')
    plt.plot(x,y,'.')
    plt.title('Ecuacion Carteciana')
    plt.xlim(-ext,ext)
    plt.ylim(-ext,ext)
    plt.grid()
    plt.show()
    return 
#=================================================================

#Parametros de entrada
#********************************
p=2          # semi-latus rectum    
e=0.2      # excentricidad
angulo=0 
#********************************

vector=conica(p,e,angulo)

print ("Discriminante %2.3f\n" %(vector[0]))
print(' A: %2.3f\n B: %2.3f\n C: %2.3f\n D: %2.3f\n E: %2.3f\n F: %2.3f\n' %(vector[1],vector[2],vector[3],vector[4],vector[5],vector[6]))

x1=vector[7]
y1=vector[8]

graf(x1,y1)

fin=time.time()
print('Tiempo de ejecucion: %2.2f segundos' %(fin-ini))

