#resorte y masa oscilando

from visual.graph import *
escena=display(width=500, height=500, range=70)

def resorteosc():
    posy=20
    longitud=80
    espesor=2
    ancho=30
    techo=box(pos=(0,posy,0), color=color.green, length=longitud,
              width=ancho, height=espesor)
    Lresorte=40
    k=10.0 #constante del resorte
    resorte=helix(pos=(0,posy,0), radius=7, color=color.orange, colis=10.4, axis=(0, -Lresorte,0),
                  thickness=1)
    curve(pos=[(0,-Lresorte,0),(0,60,0)])
    peso=10.
    masa=10.0/9.8
    Lcil=0 #longitud del cilindro
    pesa=cylinder(pos=(0,posy-Lresorte,0), radius=12, axis=(0,-Lcil,0), color=(0.5,0.5,0.5), opacity=0.7)
    cm=sphere(pos=(0,posy-Lresorte-Lcil/2.,0), radius=1, color=color.red) #esfera en el centro del cilindro
    mitadcil=vector(0,posy-Lresorte-Lcil/2)
    x=vector(0,10.0,0)+mitadcil
    mg=peso*vector(0,-1,0)
    F=-k*(x-mitadcil)+mg #fueza sobre el cilindro
    dt=0.1
    vel=vector(0,0,0)

    while true:
        rate(20)
        F=-k*(x-mitadcil)+mg #fuerza sobre el cilindro
        vel=vel+(F/masa)*dt
        x=x+vel*dt
        cm.pos=x #posicion centro de masa del cilindro
        pesa.pos=(vector(0,posy-Lresorte,0)+x-mitadcil)
        resorte.axis=vector(0,posy-Lresorte+Lcil/2.)+x

    
resorteosc()

