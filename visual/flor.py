#GENERO UNA FLOR GRAFICADA EN UN PLANO CARTECIANO.

from visual.graph import *

class OOPlanet:
    def __init__(self,rad,pomg):  #construccion del planeta
        self.Radio=rad
        self.wplaneta=pomg
    def getX(self,time):
        return self.Radio*cos(self.wplaneta*time)
    def getY(self,time):
        return self.Radio*sin(self.wplaneta*time)
    def escenario(self,mititulo,mixtitulo,miytitulo,xma,xmi,yma,ymi):
        graph=gdisplay(x=0,y=0,width=500,height=500,title='mititulo',xtitle=mixtitulo,ytitle=miytitulo,
                       xmax=xma,xmin=xmi,ymax=yma,ymin=ymi,background=color.black,foreground=color.green)
    def posicion (self):
        planetfun=gcurve(color=color.red)
        for time in arange(0,3.3,0.02):
            xp=self.getX(time)
            yp=self.getY(time)
            planetfun.plot(pos=(xp,yp))


class Luna(OOPlanet):
    def __init__(self,Rad,pomg,rl,lom):  #valores madre e hija
        OOPlanet.__init__(self,Rad,pomg) #inicializa la clase madre
        self.rad=rl
        self.omgl=lom
    def posicion(self):
        lunafun=gcurve(color=color.yellow)
        cir=gcurve(color=color.red)
        for time in arange(0,3.3,0.01):
            xm=self.getX(time)+self.rad*cos(self.omgl*time)
            ym=self.getY(time)+self.rad*sin(self.omgl*time)
            lunafun.plot(pos=(xm,ym))
            u=1.5*cos(5*time)
            v=1.5*sin(5*time)
            cir.plot(pos=(u,v))
            rate(10)

luna=Luna(4.0,2.0,1.0,14.0)
luna.escenario('Sat','x','y',5,-5,5,-5)
luna.posicion()

