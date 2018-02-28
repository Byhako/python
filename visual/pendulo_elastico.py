
#Ruben E Acosta
#1014200905
#Pendulo elastico.
#python 2.7


from visual import *
gra=gdisplay(x=500, y=0, width=400, height=300,title='X Vs. Y',xtitle='X',ytitle='Y',)
fase=gcurve(color=color.red)

gra=gdisplay(x=500, y=300, width=400, height=300,title='Amplitud',xtitle='t',ytitle='Y',)
amplitud=gcurve(color=color.blue)

scene=display(x=0, y=0, width=500, height=600, rango=1000)
scene.forward=(-0.7,-0.4,-1.2)


resorte=helix(pos=(0,15,0),radius=0.8,thickness=0.2,color=color.white,coils=15)
masa=sphere(pos=(0,-5,0),radius=2,color=color.red)
soporte=cylinder(pos=(0,15,2),color=(0.56,0.33,0),axis=(0,0,-9))
cubo=box(pos=(0,15,-7),length=3,width=3,height=3,color=(0.74,0.53,0))
pilar=cylinder(pos=(0,14,-7),axis=(0,-30,0),color=(0.56,0.33,0))
base=box(pos=(0,-16,-4),length=20,width=12,height=1,color=(0.56,0.33,0))
sup=cylinder(pos=(0,16,-7),axis=(0,1,0),color=(0.56,0.33,0))
punta1=cone(pos=(0,17,-7),axis=(0,3,0),color=(0.56,0.33,0))
punta2=cone(pos=(0,15,2),axis=(0,0,2),color=(0.56,0.33,0))
pun1=sphere(pos=(0,15,3.7),radius=0.5,color=(0.74,0.53,0))
pun2=sphere(pos=(0,19.5,-7),radius=0.5,color=(0.74,0.53,0))
pata1=box(pos=(-8.0,-17,-4),length=4,width=12,height=1,color=(0.56,0.33,0))
pata2=box(pos=(8.0,-17,-4),length=4,width=12,height=1,color=(0.56,0.33,0))
eje=curve(pos=[(0,7,0),(0,-7,0)],color=color.green)
guia1=curve(pos=[(-2,5,0),(2,5,0)],color=color.green)
guia2=curve(pos=[(-2,-5,0),(2,-5,0)],color=color.green)
guia3=curve(pos=[(-7,0,0),(7,0,0)],color=color.green)
flabel1=label(pos=(-15,-28,0),box=2, text='PENDULO ELASTICO')

"""***********************************************************************
**************************************************************************
"""
k=2.0    #constante del resorte
m=3.0    #masa de la esfera
l=15     #longutud muelle con la masa, en posicion de equilibrio.
b=0.5    #constante de amortiguamiento

y0=2     #x inicial
x0=8     #y inicial
g=9.8    #gravedad
t=0.1    #delta de tiempo
wp=(g/l) #frecuencia pendulo
wr=(k/m) #frecuencia resorte
F=b/(2*m)#gamma amortiguacion
w1=sqrt((wr**2)-((F)**2))  #resorte
w2=sqrt((wp**2)-((F)**2))  #pendulo


"""***********************************************************************
**************************************************************************
"""

while t<80:
      rate(7)
      theta=(pi/4)*cos(((g/l)**(1/2))*t) #variacion de angulo con tiempo
      y1=y0*cos(((k/m)**(1/2))*1.2*t)    #variacion de longitud con tiempo
      t=t+0.5
      x=l*sin(theta)
      y=l*cos(theta)+y1
      
      masa.pos=(x,-y+15,0)
      resorte.axis=(x,-y,0)
      amplitud.plot(pos=(t,y-12.6))
      fase.plot(pos=(x,y-12.6))
"""
#solo pendulo
while true:
      rate(10)
      theta=(pi/4)*exp(-F*t)*cos(w2*t)
      t=t+0.5
      x=l*sin(theta)
      y=l*cos(theta)
      masa.pos=(x,-y+15,0)
      resorte.axis=(x,-y,0)

#solo resorte
while True:
      rate(7)
      x=x0*exp(-F*t)*cos(w1*t)
      t=t+0.5
      masa.pos=(0,x,0)
      resorte.axis=(0,x-15,0)
"""
## 12.6 es 10.6+y0
      

