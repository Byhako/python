"""
Coeficientes de Fourier en base exponencial y trigonometrica.
Serie de Fourier para una funcion dada.
Transformada discreta de fourier.
Transformada inversa discreta de Fourier.

¡La funcion debe ser ingresada como un string y entre parentesis!

Ruben E Acosta 
Agosto 2016
"""

import numpy as np
from numpy import pi

#*******************************************************************
#        integral con simpson
#*******************************************************************
def simpson(ec,p,a,b,n):
    """
    ec -> Ecuacion a integrar
    p  -> Periodo de funcion
    a  -> Extremo inferior
    b  -> Extremo superior
    n  -> Parametro que necesita la funcion
    """
    def f(x,P=p,N=n): # P: periodo de funcion
        return eval(ec)
        
    nu=100*(b-a)
    h=(b-a)/nu
    x0=a
    I=0
    while x0<b:
        x2=x0+2*h
        x1=x0+h
        g=(h*(f(x0)+4*f(x1)+f(x2)))/3
        I=I+g
        x0=x2
    return I

#*******************************************************************
# Coeficientes en base exponencial
#*******************************************************************
def coe_ex(ec1, p, nmax, d=0):
    """
    ec1: Funcion a expandir ingresada como string
    p:  Periodo de funcion
    d: Punto minimo del intervalo de integracion.
       [0,2pi]   [-pi,pi]
    
    nmax:  Intervalo de coeficientes deseados.
    si --> [0,nmax] = [0,4] calcula:
    c0,c1,c2,c3,c4
    """    
    coeficiente = []
    xmin = d
    xmax = d+p
    
    for n in range(0,nmax+1):
        
        ec2 = '*np.exp(-2j*pi*N*x/P)' # base exponencial
        ec = ec1+ec2  # concateno las ecuaciones    
        ban = simpson(ec,p,xmin,xmax,n)
        coeficiente.append(ban/p)
                 
    return coeficiente

#******************************************************************* 
#   Serie de Fourier
#*******************************************************************   
def serie_fourier(ec,p,nmax,a,b,paso,d=0):
    """
    ec: Ecuacion a expandir.
    p:  Periodo de funcion.
    nmax: Numero maximo de la sumatoria.
    a,b: Extremos intervalo de x.
    
    d: Punto minimo del intervalo de integracion.
       [0,2pi]   [-pi,pi]
       
    Devuelvo dos vertores:
        X->valores eje x
        g->valores serie
    """
    coo = coe_ex(ec, p, nmax, d)   # Calculo coeficientes
    g = [] 
    X = np.arange(a,b,paso)
    c0 = coo[0].real

    for i in range(len(X)):
        suma = 0
        for k in range(1,nmax+1):
            ban = (coo[k]*np.exp(2j*pi*k*X[i]/p))
            suma += 2*(ban.real) 
    
        g.append(c0+suma)    
    
    return X,g    

#******************************************************************* 
        
x,r = serie_fourier('(x*x+x)', 1, 35,-2.5,2.5,0.01)        
c = coe_ex('(x*x+x)', 1, 4,-0.5)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         