#ALEJANDRO ZAPATA.

from visual import *

scene=display(x=0, y=0, width=700, height=700, rango=100)
scene.forward=(0,2,-1.2)

#====================================================================================
#====================================================================================
# formacion de la figura

base=cylinder(pos=(0,0,0), radius=20, axis=(0,0,4),color=(0.84,0.0,0.76),opacity=0.4)
iman1=cylinder(pos=(0,0,25), radius=20, axis=(0,0,2),color=color.blue)
iman2=cylinder(pos=(0,0,27), radius=20, axis=(0,0,2),color=color.red)
iman3=cylinder(pos=(0,0,-25), radius=20, axis=(0,0,2),color=color.red)
iman4=cylinder(pos=(0,0,-27), radius=20, axis=(0,0,2),color=color.blue)
separador=box(pos=(0,0,2.1),length=1,width=4.2,height=40,color=(0,0,0))
particula=sphere(pos=(0,0,2),radius=0.6,color=(0.61,1.0,0.0),make_trail=True)
particula.trail=curve(radius=10, color=color.green)
cable1=cylinder(pos=(3,-20,3), radius=0.2, axis=(0,-16,0),color=color.yellow)
cable2=cylinder(pos=(-3,-20,1), radius=0.2, axis=(0,-10,0),color=color.yellow)
cable3=cylinder(pos=(-3,-30,1), radius=0.2, axis=(-40,0,0),color=color.yellow)
cable4=cylinder(pos=(3,-36,3), radius=0.2, axis=(-46,0,0),color=color.yellow)
fuente=box(pos=(-44,-33,2),length=4,width=9,height=15,color=(0.56,0.33,0))
flecha1=arrow(pos=(20,0,20),axis=(0,0,-6),color=color.green)
flecha2=arrow(pos=(-20,0,20),axis=(0,0,-6),color=color.green)
flecha5=arrow(pos=(15,0,-16),axis=(0,0,-6),color=color.green)
flecha6=arrow(pos=(-18,0,-16),axis=(0,0,-6),color=color.green)
flecha7=arrow(pos=(0,20,-16),axis=(0,0,-6),color=color.green)
flecha12=arrow(pos=(-10,10,-10),axis=(0,0,-6),color=color.green)
flecha13=arrow(pos=(8,8,-10),axis=(0,0,-6),color=color.green)
flabel1=label(pos=(-10,-21,27),box=2, text='N')
flabel1=label(pos=(-4,-21,33),box=2, text='S')
flabel1=label(pos=(-10,-21,-23),box=2, text='N')
flabel1=label(pos=(-5,-21,-18),box=2, text='S')
flabel1=label(pos=(-47,-36,2),box=2, text='FEM')

#====================================================================================
#====================================================================================

E=2.0  #campo electrico
B=10.0  #campo magnetico
m=9.1e-31 #masa electron
q=-1.6e-19 #carga electron
v=5

for i in arange(0.0,100,0.1):  #trayecto espiral
    rate(90)
    r=(E/B)*i   
    x=r*cos(i)
    y=r*sin(i)
    particula.pos=(x,y,2)

for t in arange(0.0,10.0,0.1): #trayecto rectilineo
      rate(90)
      x1=v*0.6*t+x
      y1=v*t+y
      particula.pos=(x1,y1,2)
   

