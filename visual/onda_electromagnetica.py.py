from visual import *
xmax=201
scene=display(x=0,y=0,width=500, height=500)#grafica en dos dimensiones
scene.forward=(-1,-0.5,1)
curvaseno=curve(x=range(0,xmax), color=color.yellow,radius=4.5)#onda seno
curvacoseno=curve(x=range(0,xmax), color=color.red,radius=4.5) #onda coseno
incr=pi/xmax
for t in arange(0,100000.0,0.02): #punto flotante (arange), bucle para el tiempo
    
    for i in arange(0,xmax):
        x=i*incr             
        y=sin(6.0*x-t)        #y=f(x) plano x-y
        zz=cos(6.0*x-t)       #para la grafica z-x
        yp=100*y              #coordenadas de pantalla para y
        xp=200*x-300
        zp=100*zz
        curvaseno.x[i]=xp
        curvaseno.y[i]=yp
        curvacoseno.x[i]=xp
        curvacoseno.z[i]=zp
