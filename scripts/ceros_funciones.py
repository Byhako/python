"""
Cero de un polinomio usando biseccion y newton.

Ruben E Acosta

2016-02-27
"""

from numpy import *

print('**************************')
print('    CERO DE LA FUNCION '   )
print('**************************','\n')

 
ec=input('Escribe la funcion a resolver: ')
x1=float(input('Ingresa extremo inferior del intervalo aproximado: '))
x2=float(input('Ingresa extremo superior del intervalo aproximado: '))
errordeseado=float(input('De el error deseado: '))
x0=x1

def f(x):
    return eval(ec)
##
error=8

while error>errordeseado:
    xmed=(x1+x2)/2
    if f(xmed)==0.0:
        break
    if (f(x1)*f(xmed))<0:
        x2=xmed
    else:
        x1=xmed
    error=abs(x2-x1)
    
print ('')       
print ('La raiz por biseccion es:',round(xmed,7))
print ('')

##
h=0.0000001 
# (f(x+h)-f(x))/h usamos la definicion para calcular el valor de la derivada.

while True:
    x1=x0-(f(x0)/((f(x0+h)-f(x0))/h	))
    if x1==0.0:
        break
    error=abs(x1-x0)
    if error<errordeseado:
        break
    x0=x1  

print ('La raiz por Newton es:   ',round(x1,7))
print('')
