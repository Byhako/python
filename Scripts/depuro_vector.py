"""
LEO LOS ELEMENTOS DEL VECTOR, Y MUESTRO UNA LISTA SIN REPETIR ELEMENTOS.
OSEA, COMPARO ELEMENTO A ELEMENTO Y LO MUESTRO SOLO UNA VEZ.
EN X HAY 3 VECES EL DOS, YO SOLO LO MUESTRO UNA VEZ.

Ruben E Acosta

2016-02-27
"""
from numpy import *

x=[1,2,3,1,2,5,3,7,8,2]

lon=len(x)

for y in range(0,lon):
    con=0
    for u in range(0,y+1):
        if x[u]!=x[y]:
            con=con+1
            
    if con==y:
        print (x[y])
