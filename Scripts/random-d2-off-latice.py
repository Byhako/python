import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import interpolate
import time
inicio=time.time()

X=[0]
Y=[0]
x=0
y=0
n=150    #numero de pasos

for i in range(n):
    ban=random.random()
    theta=2.0*np.pi*ban   #angulo aleatorio
    x=x+np.cos(theta)     #paso en x
    y=y+np.sin(theta)     #paso en y
    
    X.append(x)
    Y.append(y)
    
##----------------------------------------------------
xe=np.arange(min(X)-1,max(X)+2)  
ye=np.arange(min(Y)-1,max(Y)+2)  

plt.plot(X,Y,'b-o')
plt.plot(0.0,0.0,'g-o',markersize=10.0,label='Punto inicial')  
plt.plot(x,y,'r-o',markersize=10.0,label='Punto final')  
plt.xlabel('$Steps\;on\;X$',size=22)
plt.ylabel('$Steps\;on\;Y$',size=22)
plt.legend(loc = 0)
plt.grid(True) #rectangulos grises
plt.text(x=min(X),y=max(Y),s='$Pasos = 150$',fontsize = 20)
plt.title('$\mathit{Random\;Walk\;2D\;Off-Latice}$',color='m',size=28)    
plt.xticks(xe,size=16)
plt.yticks(ye,size=16)

des=np.sqrt(x*x+y*y)
razon=(np.sqrt(des))/(np.sqrt(n))
print(razon)
fin=time.time()
print('Tiempo de ejecucion: %2.2f segundos' %(fin-inicio))