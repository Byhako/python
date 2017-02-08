#superpone dos funciones seno

from visual.graph import *

class Superposicion: #Se va a definir una clase
    def __init__(self,Am1,Am2,frec1,frec2,alf2): #Un constructor de la clase , que inicializa los valores de la clase
        self.A1=Am1
        self.A2=Am2
        self.f1=frec1
        self.f2=frec2
        self.a=alf2
    def posx(self,t):
        return self.A1*cos(self.f1*t) # posicion en x:A1cos(f1*t)
    def posy(self,t):
        return self.A2*cos(self.f2*t+self.a) #Poscion en y:A2cos(f2*t+alfa)
    def sumacosenos(self, mytitle, myxtitle,myytitle,
                xma, xmi, yma, ymi): #nombres del eje x, eje y; minimo x..
        graph=gdisplay(x=0, y=0, width=500, height=500,
                       title=mytitle, xtitle=myxtitle, ytitle=myytitle,
                       xmax=xma, xmin=xmi, ymax=yma, ymin=ymi,
                       foreground=color.black, background=color.white)
        funcion=gcurve(color=color.red)

        for t in arange(0.,6.5,0.01):
            rate(40)
            for x in range(0,10):
                x=x+1
            for y in range(0,10):
                y=y+1
            x=self.posy(t)
            y=self.posx(t)
            funcion.plot(pos=(x,y))

#Todo lo anterior es abstracto. A continuacion daremos valores

figura=Superposicion(1.0,1.5,1.0,2.0,pi/2.)
figura.sumacosenos('Superposicion de dos cosenos', 'x', 'y', 2,-2,2,-2) #para gaficar

            
        
