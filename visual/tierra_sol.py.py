#movimiento de la tierra alrededor del sol

from visual.graph import *

scene=display(x=0, y=0, width=700, height=500, rango=500)

sol=sphere(pos=(0,0,0), radius=20, color=color.yellow)
rfactor=2.0e-9 #factor para la escala de mi dibujo. Este factor para todo lo que pinto
G=6.67e-11 #m**3/Kgs**2
m=6.6e24 #masa de la tierra
M=2.0e30 #masa de sol
veloc=29780.0 #m/s velocidad orbital de la tierra
d=1.5e11 #disrancia tierra sol en m
dp=d*rfactor
tierra=sphere(pos=(0,dp,0), radius=10, color=color.cyan, make_trail=True) #make_trail deja una traza por el recorrido orbital de la tierra
velo= vector(veloc,0,0) #vector velocidad de la tierra
dt=86400.0 #segundos en un dia
r=vector(0,d,0) #vector posicion de la tierra
dtl=3.84e8 #en metros distancia tierra luna
ml=7.35e22 #en kg masa de la luna
veluna=1023.0 #en metros la velocidad de la luna
lunfactor=1.5e-8 #factor para pintar la luna
dpluna=dtl*lunfactor #distancia a escala entre tierra y luna
luna=sphere(pos=(0,dp+dpluna,0),radius=5, color=color.white, make_trail=True)
rluna=vector(0,dtl,0) #luna respecto a tierra
vel=vector(veluna,0,0)


for i in range(0,365):
    rate(10)
    F=-G*M*m*r/(d**3) #fuerza sobre la tierra
    acel=F/m #aceleracion centripera
    velo = velo+acel*dt #nueva velocidad
    r = r + velo*dt
    rc = r*rfactor
    tierra.pos=rc
    Ftl=-G*m*ml*rluna/(dtl**3)
    acluna=Ftl/ml+F/m #aceleracion de la luna
    vel=vel+(acluna+acel)*dt
    rluna= rluna + vel*dt
    rc = rc+rluna*lunfactor #en coordenadas de pantalla
    luna.pos=rc
