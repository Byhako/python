#efecto de campo magnetico sobre carga

from visual.graph import *
import random

scene=display(x=0,y=0,width=500,height=500,title='Campo B',range=(600)) #inicia en (0,0)

B=vector(0,0,-15) #vector del campo magnetico. El campo entra a la pantalla
dt=0.02 #incremento (o intervalo) en el tiempo
carga=1.0 #carga positiva
r=vector(0,0,0) #vector posicion de la carga
trayec=curve(color=color.red) #trayectoria que sigue la carga
bola=sphere(radius=10) #carga electrica
bola.trail=curve(radius=10, color=color.red) #.trail, para que deje una trayectoria
vel=1000*vector(2*random.random()-1.0, 2*random.random()-1.0,0.5*(2*random.random()-1.0)) #con random.random()-1.0 es truco para que el numero salga entre 0 y uno
curve(pos=[(-500,0,0),(500,0,0)]) #dibuja un eje
for i in range(0,100):
    rate(10)
    bola.pos=r #calcula la posicion de la particula
    bola.trail.append(pos=r) #que pinte trayectoria
    r=r+vel*dt #nueva posicion
    a=carga*vel.cross(B) #prodyucti cruz a=qvXB; donde la masa de la particula es 1
    vel=vel+a*dt
