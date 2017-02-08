#ilustra los arreglos (arreu), es decir: las variables indexadas

from visual.graph import *

grapico=gdisplay(width=500, height=300, title='y Vs t', xmin=0, xmax=20, ymin=0, ymax=2000)

posicion= gcurve(color=color.red)

velocidad= gdisplay(x=0, y=300, width=500, height=300, title=' v Vs t', xmin=0, xmax=20, ymin=0, ymax=500)

velo=gcurve(color=color.green, display=velocidad) #para pintar la grafica

aceleracion= gdisplay(x=0, y=600, width=500, height=300, title='a Vs t', xmin=0, xmax=20, ymin=0, ymax=10)

acel=gcurve(color=color.magenta, display=aceleracion)

#definimos las varables

y=zeros((20), float) #posiciones

v=zeros((20), float) #velocidad

a=zeros((20), float) #aceleracion

t=0 #tiempo inicial
dt=1 #incremento en el tiempo

for i in range (0,20):
    y[i] = 9.8*t*t/2.0 #posicion al caer
    posicion.plot(pos=(t,y[i])) #pinta la curva posicion 
    t=t+1 #incremento en un segundo. Tambien podemos escribir t+=1

t=0
for i in range (0,20):  #muestra los valores de t y la variable suscrita(t, y[i])
    print(t,y[i])
    t=t+1

t=0
for i in range (1,20):
    v[i]= (y[i]-y[i-1]/dt)
    velo.plot(pos=(t,v[i]))
    t=t+1

t=0
for i in range (2,20):
    a[i]= (v[i]-v[i-1]/dt)
    acel.plot(pos=(t,a[i]))
    t=t+1
                   
    
