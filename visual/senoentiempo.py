

from visual.graph import *
vantana=gdisplay(x=0,y=0,width=500,xmin=-90*pi,xmax=90*pi,
                 ymin=-1,ymax=1,title="sen")
grafico=gcurve(color=color.blue)
for x in arange(-90*pi,90*pi,0.1):
   y=sin(x)# funcion seno
   rate(15)# demora para que se haga la grafica si algo la cambias
   grafico.plot(pos=(x,y))
   
