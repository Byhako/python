'''
1) Triangulo equilatero de lado 1
2) Numerar vertices 1,2,3 con coordenadas (a1,b1),(a2,b2),(a3,b3)
3) Generar un numero aleatorio r
4) Para escoger con r un vertice
5) Se traza imaginariamente recta entre vertice generado aleatoriamente y
   el punto P que está dentro del triangulo
6) Se halla el punto medio de la recta que une el vertice con P.
   El punto medio es el nuevo punto P
7) Se repiten los pasos del 3 al 6.
'''

from visual.graph import *
import random

graph=display(width=1000,height=1000,range=0.6)

x=0.0   #Punto P inicial
y=0.0   #Punto P inicial
a1=-0.5
b1=-0.433012701
a2=0.5
b2=-0.433012701
a3=0.0
b3=0.433012701

for i in range(1,100000):
    r=random.random()
    r=int(3*r)+1
    if r==1:
        x=(a1+x)/2.0
        y=(b1+y)/2.0
    elif r==2:
        x=(a2+x)/2.0
        y=(b2+y)/2.0
    else:
        x=(a3+x)/2.0
        y=(b3+y)/2.0
    points(pos=(x,y),size=1,color=color.red)

