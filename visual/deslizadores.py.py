
#efecto de deslizadores (slider)

from visual.graph import *
from visual.controls import *

escena=display(width=600, hight=600, range=100) #para pintar
escena.center=(0,0,200) #trae curve pos a la posicion (0,0,200)
piramide=pyramid(pos=(-50,0,0),size=(100,50,200))





caja=[]   #lista vacía
curve(pos=[(-250,-250,250),(250,-250,250),(250,250,250),
           (-250,250,250),(-250,-250,250)])
curve(pos=[(-250,-250,-250),(250,-250,-250),(250,250,-250),
           (-250,250,-250),(-250,-250,-250)])
C=controls(title='colores', x=600, y=0, width=300, height=300, range=255)
def escojaro(obj):
    return obj.value
def escojaz(obj):
    return obj.value
def escojaver(obj):
    return obj.value

#Deslizadores
ro=slider(pos=(-200,-200,0),length=300,axis=(0,1,0), min=0,
          max=1, action=lambda:escojaro(ro), width=30, color=color.red)
az=slider(pos=(200,-200,0),length=300,axis=(0,1,0), min=0,
          max=1, action=lambda:escojaz(az), width=30, color=color.blue)
ver=slider(pos=(0,-200,0),length=300,axis=(0,1,0), min=0,
          max=1, action=lambda:escojaver(ver), width=30, color=color.green)

ro.value=1.0
fac=500.0 #factor para escala


while True:
    rate(50)
    rojo=escojaro(ro)
    verde=escojaver(ver)
    azul=escojaz(az)
    ropos=rojo
    azpos=azul
    verpos=verde
    piramide.color=(rojo,verde,azul)
   
    
    

