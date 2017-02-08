#Equilibrio de fuerzas

from visual.graph import *
escena=display(height=600, width=600, rango=380)

#Grafica

posy=100#altura base
Lhilo=250 #longitud del hilo
divi=curve(pos=[(0,-150,0),(0,100,0)]) #eje simetria
alt=curve(pos=[(-300,posy,0),(300,posy,0)]) #altura
Lpesa=50 #altura pesa (cilindro). Altura cilindro
pesa=cylinder(pos=(0,posy-Lhilo,0), radius=20, color=color.red,
              axis=(0,-Lpesa,0)) #con axis cambiamos la direccion original en que se pinta el cilindro
hilo1=cylinder(pos=(0,posy,0),axis=(0,-Lhilo,0), color=color.yellow,
               radius=2) #en el eje solo colocamosdesde el SR de nuestra grafica
hilo2=cylinder(pos=(0,posy,0),axis=(0,-Lhilo,0), color=color.yellow,
               radius=2)
flecha1=arrow(pos=(0,posy,0), color=color.orange)
flecha2=arrow(pos=(0,posy,0), color=color.orange)

peso=10.
magF=peso/2.0 #al omienzo
velocidad=2.0 #velocidad de desplazamiento de un estudiante
x1=0.0 #posicion inicial de un estudiante

#letrero
flabel1=label(pos=(200,240,0),box=0, text='Fuerza')
flabel2=label(pos=(-200,240,0),box=0, text='Fuerza')
fText1=label(pos=(200,210,0),box=0)
fText2=label(pos=(-200,210,0),box=0)
angtext=label(pos=(20,210,0),box=0)
anglabel=label(pos=(0,240,0), text='Theta', box=0)
local_light(pos=(0,0,20), color=color.green) #coloca una lampara en un punto para que alumbre


#descripcion del movimiento
for t in arange(0.,125.,0.2):
    rate(100) #demora la vista
    x1=velocidad*t
    hilo1.pos=(x1,posy,0)
    hilo2.pos=(-x1,posy,0)
    theta=asin(x1/Lhilo) #en radianes
    angulo=(theta*180.)/pi #lo convertimos en grados
    magF=peso/(2.0*cos(theta)) #Fuerza variable
    poscil=posy-Lhilo*cos(theta)
    pesa.pos=(0,poscil,0) #pintar la posicion de la pesa
    hilo1.axis=(-x1,-Lhilo*cos(theta),0)
    hilo2.axis=(x1,-Lhilo*cos(theta),0)
    flecha1.pos=hilo1.pos
    flecha2.pos=hilo2.pos
    flecha1.axis=(8*magF*sin(theta),8*magF*cos(theta))
    flecha2.axis=(-8*magF*sin(theta),8*magF*cos(theta))
    fuerza=magF
    fText1.text='%8.2f' %fuerza
    angtext.text='%4.2f' %angulo
    fText2.text='%8.2f' %fuerza
    



