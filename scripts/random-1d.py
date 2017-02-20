import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import interpolate
import time
inicio=time.time()
m=150          #numero de pasos
p=1.0/2.0      #parametro probabilidad     
##--------------------------------------------------------------
R=0.0      #desplazamiento acumulado
n1=0       #contador de pasos
x1=[0.0]   
N1=[0.0]

while n1<m+1:
    ban=random.random()  #num aleatorio en [0,9]
    
    if ban<p:
        x=1        #paso arriba
    else:
        x=-1       #paso abajo
   
    n1=n1+1
    R=R+x
    x1.append(R)
    N1.append(n1)
##--------------------------------------------------------------
R=0.0      #desplazamiento acumulado
n2=0       #contador de pasos
x2=[0.0]   
N2=[0.0]

while n2<m+1:
    ban=random.random()  #num aleatorio en [0,9]
    
    if ban<p:
        x=1        #paso arriba
    else:
        x=-1       #paso abajo
   
    n2=n2+1
    R=R+x
    x2.append(R)
    N2.append(n2)
##--------------------------------------------------------------
R=0.0      #desplazamiento acumulado
n3=0       #contador de pasos
x3=[0.0]   
N3=[0.0]

while n3<m+1:
    ban=random.random()  #num aleatorio en [0,9]
    
    if ban<p:
        x=1        #paso arriba
    else:
        x=-1       #paso abajo
   
    n3=n3+1
    R=R+x
    x3.append(R)
    N3.append(n3)
##--------------------------------------------------------------
R=0.0      #desplazamiento acumulado
n4=0       #contador de pasos
x4=[0.0]   
N4=[0.0]

while n4<m+1:
    ban=random.random()  #num aleatorio en [0,9]
    
    if ban<p:
        x=1        #paso arriba
    else:
        x=-1       #paso abajo
   
    n4=n4+1
    R=R+x
    x4.append(R)
    N4.append(n4)
##--------------------------------------------------------------
R=0.0      #desplazamiento acumulado
n5=0       #contador de pasos
x5=[0.0]   
N5=[0.0]

while n5<m+1:
    ban=random.random()  #num aleatorio en [0,9]
    
    if ban<p:
        x=1        #paso arriba
    else:
        x=-1       #paso abajo
   
    n5=n5+1
    R=R+x
    x5.append(R)
    N5.append(n5)
##--------------------------------------------------------------
maximos=[max(x1),min(x1),max(x2),min(x2),max(x3),min(x3),max(x4),min(x4),max(x5),min(x5)]
ejey=np.sort(maximos)  #ordenar lista acendentemente
xt=np.arange(0,m+m/15.0,m/15.0)
plt.subplot(211)
plt.plot(N1,x1,'b')
plt.plot(N2,x2,'r')
plt.plot(N3,x3,'y')
plt.plot(N4,x4,'g')
plt.plot(N5,x5,'k')
plt.axis([0,m+1,ejey[0]-5,ejey[9]+5])
plt.ylabel('$Displacement$',size=22)
plt.xlabel('$Steps$',size=22)
plt.xticks(xt,size=16)
plt.yticks(size=16)
plt.title('$\mathit{Random\;Walk\;1D\;p=1/2\;q=1/2}$ ',color='m',size=28)

##--------------------------------------------------------------
#Repito lo anterios 30000 veces para hacer histrograma
desplaza=[]
for i in range(30000):
    R=0.0      #desplazamiento acumulado
    n=0        #contador de pasos

    while n<m+1:
        ban1=random.random()
    
        if ban1<p:
            x=1
        else:
            x=-1
   
        n=n+1
        R=R+x

    desplaza.append(R) 
##--------------------------------------------------------------
##Histograma

a=int(min(desplaza))
b=int(max(desplaza))
k=0
frecuencia=[]
d=[]
for i in range(a,b+1):
    con=0
    for j in range(len(desplaza)):
        if i==desplaza[j]:
            con=con+1

    frecuencia.append(con)
    d.append(i)
  
##--------------------------------------------------------------     
##envolvente  spline
y=[]
d1=[]
for i in range(len(frecuencia)):
    if frecuencia[i]!=0:   #excluir datos con valor cero
        y.append(frecuencia[i]+10)
        d1.append(d[i])
tck = interpolate.splrep(d1, y, s=0)
xnew = np.arange(a,b,0.001)
ynew = interpolate.splev(xnew, tck, der=0)

##--------------------------------------------------------------
plt.subplot(212)
ymax=max(frecuencia)+(max(frecuencia)/10)
plt.bar(d,frecuencia, align='center',width=1.5,color='red')
plt.plot(xnew,ynew,linewidth=1.5)
plt.axis([a-1,b+1,0,ymax])
plt.xlabel('$Displacement$',size=22)
plt.ylabel('$Frequency$',size=22)
plt.xticks(d1,rotation='vertical',size=16)
plt.yticks(size=16)
plt.show()


fin=time.time()
print(('Tiempo de ejecucion: %2.2f segundos') %(fin-inicio))