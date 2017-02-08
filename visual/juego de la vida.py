# automatas celulares  conway  juego de la vida

from visual.graph import *
import random

scene=display(width=500, height=500, title='juego de la vida')
cell=zeros((50,50)) #primera distribucion todas 0
boxes=points(shape='square',size=8,color=color.cyan) #pequeñas cajas de dos dim
curve(pos=[(-49,-49),(-49,49), (49,49), (49,-49)])
def drawcells(ce):  #pintar las celdas le entran ce
    box.pos=[]  # borra las celdas anteriores,  lista vacia
    for j in range(0,50):  #filas
        for i in range(0,50): #columnas
            if ce[i,j]==1:
                xx=2*i-50 # transferencia de coordenada x
                yy=2*j-50  # transferencia de coordenada y
                boxes.append(pos=(xx,yy)) #pone cajas en posiscion

def inicial():
    for j in range(20,28):
        for i in range(20,28):
            r=int(random.random()*2) # para obtener 0 o 1
            cell[j,i]=r
    return cell

temp=inicial()
drawcells(temp)

def juegovida(cell):
    for i in range(1,49):
        for j in range(1,49):
            sum1=cell[i-1,j-1]+cell[i,j-1]+cell[i+1,j-1]
            sum2=cell[i-1,j]+cel[i+1,j]+cel[i-j,j+1]+cel[i,j+1]+cell[i+1,j+1]
            vivas=suma1+suma2 #celdas vecinas vivas
            if cell[i,j]==1: #celda[i,j] esta viva?
                if vivas==2 or vivas==3: #2 o 3 vivas
                    cellu[i,j]=1 #sigue viva. celu es la nueva situacion de cell
                if vivas>3 or vivas<2: #muere por sobrepoblada o soledad
                    cellu[i,j]=0 #la celda se muere
            if cell[i,j]==0:
                if vivas==3:
                    cellu[i,j]==1
                else:
                    cellu[i,j]==0
    vivas=0
    return cellu
    temp=inicial()
    cellu=zeros((50,50))

while True:
    rate(6)
    cell = temp
    temp = juegovida(cell)
    drawcells(cell)
            
