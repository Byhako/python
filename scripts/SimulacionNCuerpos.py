"""
Problema de los tres cuerpos.

Ruben E Acosta.

2016-02-27
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy.linalg import norm


# Ecuaciones diferenciales
def body3(y,t,parametros):
    masa=parametros['masas']
    
    r1=y[0:3]
    r2=y[3:6]
    r3=y[6:9]
    
    v1=y[9:12]
    v2=y[12:15]
    v3=y[15:18]

    a1=(masa[1]*(r2-r1)/norm(r2-r1)**3 + masa[2]*(r3-r1)/norm(r3-r1)**3)
    a2=(masa[0]*(r1-r2)/norm(r1-r2)**3 + masa[2]*(r3-r2)/norm(r3-r2)**3)
    a3=(masa[0]*(r1-r3)/norm(r1-r3)**3 + masa[1]*(r2-r3)/norm(r2-r3)**3)

    return v1.tolist()+v2.tolist()+v3.tolist()+a1.tolist()+a2.tolist()+a3.tolist()

# Propiedades y condiciones iniciales
parametros={'masas':[1.0,1.0,2.0]}

r1=[1,0,0]
v1=[0,1,0]

r2=[-1,0,0]
v2=[0,-1,0]

r3=[0.5,0,0]
v3=[0,0,1]

ys=r1+r2+r3+v1+v2+v3
ts=np.linspace(0,10,1000)

solucion=odeint(body3,ys,ts,args=(parametros,))

# Extraer trayectorias de la solución
r1s = solucion[:,0:3]
r2s = solucion[:,3:6]
r3s = solucion[:,6:9]

# Graficar en 2D
fig = plt.figure(figsize=(6,6))
ax=fig.gca()

ax.plot(r1s[:,0],r1s[:,1])
ax.plot(r2s[:,0],r2s[:,1])
ax.plot(r3s[:,0],r3s[:,1])

ext=2
ax.set_xlim(-ext,ext)
ax.set_ylim(-ext,ext)

# Graficar en 3D
fig = plt.figure(figsize=(6,6))
ax=Axes3D(fig)

ax.plot(r1s[:,0],r1s[:,1],r1s[:,2])
ax.plot(r2s[:,0],r2s[:,1],r2s[:,2])
ax.plot(r3s[:,0],r3s[:,1],r3s[:,2])

ax.view_init(elev=30,azim=60)

ext=2
ax.set_xlim(-ext,ext)
ax.set_ylim(-ext,ext)
ax.set_zlim(-ext,ext)



