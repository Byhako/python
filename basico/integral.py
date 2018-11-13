"""
Tengo 4 metodos de hacer integrales. Simpson 2, punto medio, trapecio
y monte carlo crudo.

Ruben E Acosta.

2016-02-27
"""

import numpy as np

def f(x):
      y=x**6-3*x**5-5*x**4+15*x**3+4*x*x-12*x
      return y


#****************************************
#        integral con simpson
#****************************************
def simpson(a,b):
      """
      a -> Extremo inferior
      b -> Extremo superior
      """
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

#****************************************
#         integral punto medio.
#****************************************
def puntom(a,b):
      """
      a -> Extremo inferior
      b -> Extremo superior
      """
            
      n=1000  #catidad de sub intervalos
      delta=(b-a)/n #1000 sub intervalos
      suma=0
      for i in range(n):
            x1=a+delta*i
            x2=a+delta*(i+1)
            x=(x2+x1)/2
            area=f(x)*delta
            suma=suma+area
      
      return suma

#****************************************
#     integral trapecio compuesto
#****************************************
def trape(a,b):
      """
      a -> Extremo inferior
      b -> Extremo superior
      """
      n=1000
      H=(b-a)/n
      suma1=0

      for j in range(n-1):
            c=f(a+j*H)
            suma1=suma1+c

      tra = H * ( ((f(a)+f(b)) /2) + (suma1))
      return tra

#****************************************
#          Monte Carlo crudo
#****************************************
def mc(a,b):
      """
      a -> Extremo inferior
      b -> Extremo superior
      """
      m=1000*(b-a)  #numero de datos aleatorios
      #vector aleatorio
      p=np.random.random(m)
      x=p*(b-a)+a
      num=0
      for i in range(m):
            num=num+f(x[i])
      
      area=(num/m)*(b-a)
      
      return area
      
#==================================================

a=-2 #Extremo inferior
b=3  #Extremo superior

s=simpson(a,b)
pm=puntom(a,b)
trapecio=trape(a,b)
mcarlo=mc(a,b)

print('simpson 2:      %3.5f '%(s))
print('punto medio:    %3.5f ' %(pm))
print('trapecio:       %3.5f' %(trapecio))
print('MC crudo:       %3.5f' %(mcarlo))     
