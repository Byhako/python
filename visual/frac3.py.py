from visual.graph import *
import random

graph=display(width=1000,height=1000)

x=0.0
y=0.0

for i in range (0,10000):
    r=random.random()
    if r<0.2:
        x=0.05*x
        y=0.6*y
        
    elif r>=0.2 and r<0.3:
        x= 0.05*x
        y=-0.5*y+1.0
      
    elif r>=0.3 and r<0.7:
        x=0.46*x-0.15*y
        y=0.39*x+0.38*y+0.6
    elif r>=0.7 and r<0.8:
        x=0.47*x-0.15*y
        y=-0.17*x+0.42*y+1.1

    elif r>=0.8 and r<0.9:
        x=0.43*x+0.28*y
        y=-0.25*x+0.45*y+1.0

    else:
        x=0.42*x+0.26*y
        y=-0.35*x+0.31*y+0.7

    points(pos=(2*x,2*y-0.7),size=1,color=color.red)

