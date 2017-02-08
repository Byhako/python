'''
Si la probabilidad es del 10%
    x=0
    y=0.18*y
    z=0

Si la probabilidad es del 60%
    x=-0.85*x
    y=-0.85*y+0.1z+1.6
    z=-0.1y+0.85z

Si la probabilidad es del 15%
    x=0.2*x-0.2*y
    y=0.2*x+0.2*y+0.8
    z=0.3z

Si la probabilidad es de 15%
    x=-0.02x+0.02y
    y=0.2x+0.2y+0.8
    z=0.3z


'''

from visual.graph import *
import random

graph=display(width=1000,height=1000)

x=0.5
y=0.0
z=0.5

for i in range (0,10000):
    r=random.random()
    if r<0.1:
        x=0
        y=0.18*y
        z=0
        
        
    elif r>=0.1 and r<0.7:
        x=0.85*x
        y=0.85*y+0.1*z+1.6
        z=-0.1*y+0.85*z
        
        
    elif r>=0.7 and r<0.85:
        x=0.2*x-0.2*y
        y=0.2*x+0.2*y+0.8
        z=0.3*z
        
        
    else:
        x=-0.2*x+0.2*y
        y=0.2*x+0.2*y+0.8
        z=0.3*z
        
        
    points(pos=(5*x,4*y,2*z),size=2,color=color.red)
