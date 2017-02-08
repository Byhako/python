'''
Si la probabilidad es del 20%
    x=0.01*x
    y=0.45*y

Si la probabilidad es del 10%
    x=-0.01*x
    y=-0.45*y+0.4

Si la probabilidad es del 40%
    x=0.42*x-0.42*y
    y=0.45*x+0.42*y+0.4

Si la probabilidad es del 30%
    x=0.42*x+0.42*y
    y=-0.42*x+0.42*y+0.4
'''

from visual.graph import *
import random

graph=display(width=1000,height=1000)

x=0.0
y=0.0

for i in range (0,10000):
    r=random.random()
    if r<0.2:
        x=0.01*x
        y=0.45*y
        
    elif r>=0.2 and r<0.3:
        x=-0.01*x
        y=-0.45*y+0.4
        
    elif r>=0.3 and r<0.7:
        x=0.42*x-0.42*y
        y=0.42*x+0.42*y+0.4
        
    else:
        x=0.42*x+0.42*y
        y=-0.42*x+0.42*y+0.4
        
    points(pos=(2*x,2*y-0.7),size=1,color=color.red)
