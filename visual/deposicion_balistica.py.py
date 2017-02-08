#deposicion balística

from visual.graph import *
import random

escena=display(width=500,height=500,range=250)
h=zeros((200)) #columnas en donde se depositan las particulas. Ojo:SON ENTEROS
pts=points(color=color.green, sice=2)

for i in range(0,10000): #genera 10.000 puntos aleatorios
    rate(50)
    r=int(200*random.random()) #Genera entre 0 y 199. int vuelve entero lo de dentro del parentesis. 
    if r>0 and r<199: #ojo porque no existe h[-1] = ?
        if h[r]<h[r-1] and h[r]<h[r+1]: #la columna del centro es menor que las del lado, entonces:
            if h[r+1] > h[r-1]:  
                h[r] = h[r+1] #la columna del centro es igual a la columna mas grande(la de la derecha)
            else:
                h[r] = h[r-1] #la columna del centro es igual a la columna mas grande (la de la izquierda)
        else:
            h[r]+=1 #le aumenta una bolita al grafico 
    xx=2*r-200 #escala para pintar
    yy=2*h[r]-200 #escala para pintar
    pts.append(pos=(xx,yy)) #pinta
