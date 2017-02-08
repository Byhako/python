
#INTERPOLACION CON EL POLINOMIO DE LAGRANGE
# -*- coding: utf-8 -*-
'''
Usar el método de Lagrange para encontrar una funcion g(x) tal que pase
por todos los siguiente puntos:
x   g(x)
0   10.6
25  6.0
50  45.0
75  83.5
100 52.8
125 19.9
150 10.8
175 8.25
200 4.7
'''

from visual.graph import *

scene=gdisplay(x=0,y=0,width=500,height=500,xmin=0,xmax=200,ymin=0,ymax=90)
graph=gcurve(color=color.red)
xin=array([0,25,50,75,100,125,150,175,200])
yin=array([10.6,6.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7])
yy=zeros((204),float)   #para graficar
def puntos():   #puntos experimentales
    for i in range (0,9):
        xc=xin[i]
        yc=yin[i]
        gcurve(pos=[(xc-2,yc),(xc+2,yc)])
        gcurve(pos=[(xc,yc+1),(xc,yc-1)])
def lagrangepol(x):
    y=0.
    for i in range (0,9):   #para los 8 lambdas
        lambd=1.
        for j in range(0,9):
            if i!=j:
                lambd*=((x-xin[j])/(xin[i]-xin[j]))     #Halla lambda
        y+=(yin[i]*lambd)   #g[i]*lambda[i]
    return y
def plotpoly(): #pinta polinomio
    puntos()
    xx=0.
    for k in range (0,201):
        yy[k]=lagrangepol(xx)
        graph.plot(pos=(xx,yy[k]))
        xx+=1.
plotpoly()
print lagrangepol(140.)
                
