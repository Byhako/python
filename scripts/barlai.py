"""
Traducidas del codigo original en MATLAB a python por:
Alejandro Velez Zea
velezphysics@gmail.com
REVISION DE BIBLIOTECA ( R.A enero 2014)
"""

import numpy as np
import Image as im
import pylab as py

#Crea el espacio de frecuencias para la transformada de fourier.
def espaciof(m):
    U=np.arange(m)
    for i in U:
        if U[i] > m/2:
            U[i]=U[i]-m
    U,V=np.meshgrid(U,U)
    return U

#Usa la ecuacion de difraccion de fresnel para simular la propagacion de un campo en el espacio libre
#de un plano 0 a otro z.
def propagar(pix,wl,z,I):
    I=np.asarray(I)																
    m,n=I.shape
    nt=2*m
    wlmin=2*pix
    fmax=1/wlmin
    pixfre=fmax/m
    U=espaciof(nt)
    U=pixfre*U
    # funcion de transferencia
    H=np.exp((1j*2*np.pi*z/wl)+(-1j*np.pi*wl*z)*(U**2+ np.transpose(U)**2))
    TFdat=np.fft.fft2(I,(nt,nt))    # transformada Fourier 2-d
    pro=H*TFdat
    I=np.fft.ifft2(pro)  
    IS=I[:m,:n]  # redimencionamos
    IS=np.round(IS,4)
    return IS
"""
primero se calcula la funcion de transferencia H, luego se
toma la TF2 del campo y los multiplicamos, luego se toma TIF2
de eso y tenemos la formula de difraccion.
"""    
    
#Genera un array de numpy que contiene los valores de la transformacion de fase que incurre un
#campo al atravesar un lente.	(muestreo,lamda,x,y,foco)
def lente(pix,wl,sx,sy,f):														
    x=pix*np.arange(sx)-pix*(sx/2)
    y=pix*np.arange(sy)-pix*(sy/2)
    px, py = np.meshgrid(x, y)
    phi=(np.pi/(wl*f))*(px**2+py**2)
    lens=np.exp(-1j*phi)
    return lens
    
#Funcion que simula la transformada de fourier que sufre el campo al propagarse por un lente.
#La entrada puede ser una imagen en escala de grises de PIL (modo "L") o un array de numpy.
#La salida es una array de numpy.

def tfoptica(pix,wl,f,I):
    I=np.asarray(I)
    m,n=I.shape
    lent=lente(pix,wl,n,m,f)
    IS=propagar(pix,wl,f,I)
    I=IS*lent
    IS=propagar(pix,wl,f,I)
    return IS   

#Ubica el centro de la imagen I como origen, y remplaza en I
#lo que tiene A, centrando A en las coordenadas x,y.
def fusion(x,y,A,I):
    I=np.asarray(I)  #transforma I a matriz
    m,n=I.shape      # m=#filas de I, n=#columnas de I
    A=np.asarray(A)  #transforma A en matriz
    r,t=A.shape      # filas y columnas
    E=I
    if np.remainder(r,2) == 1: # r impar
        if np.remainder(t,2)==1: # t impar
            E[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]=A
        if np.remainder(t,2)==0:  # t par
            E[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]=A
    if np.remainder(r,2) ==0: 
        if np.remainder(t,2)==1:
            E[round(m/2-r/2)+round(y):round(m/2+r/2)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]=A
        if np.remainder(t,2)==0:
            E[round(m/2-r/2)-round(y):round(m/2+r/2)-round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]=A
    E=im.fromarray(E)
    return E    
"""
remainder(i,j)=i-floor(i/j)*j
remainder(i,j) arroja 0 cuando i es divisible por j.

round si es para redondea arriba y si es impar redondea abajo, por eso
en los impares sumamos 1 (podria restar 1 en pares)
"""

# igual pero devuelve un array
def fusion2(x,y,A,I):
    I=np.asarray(I)
    m,n=I.shape
    A=np.asarray(A)
    r,t=A.shape
    y=y
    E=I
    if np.remainder(r,2) == 1:
        if np.remainder(t,2)==1:
            E[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]=A
        if np.remainder(t,2)==0:
            E[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]=A
    if np.remainder(r,2) ==0:
        if np.remainder(t,2)==1:
            E[round(m/2-r/2)+round(y):round(m/2+r/2)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]=A
        if np.remainder(t,2)==0:
            E[round(m/2-r/2)-round(y):round(m/2+r/2)-round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]=A
    return E


def tajada(x,y,A,I):
    I=np.asarray(I)
    m,n=I.shape
    A=np.asarray(A)
    r,t=A.shape
    E=A
    if np.remainder(r,2) == 1:
        if np.remainder(t,2)==1:
            E=I[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]
        if np.remainder(t,2)==0:
            E=I[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]
    if np.remainder(r,2) ==0:
        if np.remainder(t,2)==1:
            E=I[round(m/2-r/2)+round(y):round(m/2+r/2)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]
        if np.remainder(t,2)==0:
            E=I[round(m/2-r/2)-round(y):round(m/2+r/2)-round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]
    E=im.fromarray(E)
    return E

def tajada2(x,y,A,I):
    I=np.asarray(I)
    m,n=I.shape
    A=np.asarray(A)
    r,t=A.shape
    E=np.copy(A)
    if np.remainder(r,2) == 1:
        if np.remainder(t,2)==1:
            E=I[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]
        if np.remainder(t,2)==0:
            E=I[round(m/2-r/2)+round(y):round(m/2+r/2+1)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]
    if np.remainder(r,2) ==0:
        if np.remainder(t,2)==1:
            E=I[round(m/2-r/2)+round(y):round(m/2+r/2)+round(y),round(n/2-t/2)+round(x):round(n/2+t/2+1)+round(x)]
        if np.remainder(t,2)==0:
            E=I[round(m/2-r/2)-round(y):round(m/2+r/2)-round(y),round(n/2-t/2)+round(x):round(n/2+t/2)+round(x)]
    return E

def tajada3(x,y,A,I):
    A=np.asarray(A)
    r,t=A.shape
    E=I[x:r+x,y:t+y]
    E=im.fromarray(E)
    return E

def tajada4(x,y,A,I):
    A=np.asarray(A)
    r,t=A.shape
    E=I[x:r+x,y:t+y]
    return E
    
def oplana(pix,tam,a1,a2):
    t=tam.shape[1]
    n=t
    if np.remainder(n,2)==0:
        fx1=np.arange(-pix*(n/2),0+pix,pix)
        fx1=fx1[0:round(n/2)]
        fx2=np.arange(pix,pix*n/2+pix,pix)
        fx2=fx2[0:n/2]
        fx=np.concatenate((fx1,fx2))
    else:
        fx2=np.arange(0,pix*(n/2)+pix,pix)
        fx1=np.arange(-fx2[np.ceil(n/2)-1],0+pix,pix)
        fx1=fx1[0:np.ceil(n/2)]
        fx=np.concatenate((fx1,fx2))
    fy=fx
    FX,FY=np.meshgrid(fx,fy)
    oplana=1*np.exp(-1j*2*np.pi*(np.sin(a2)*FX+np.sin(a2)*FY)/WL)
    iplana=oplana*np.conj(oplana)
    return oplana,iplana


def mostrar(I):
    py.imshow(I,origin='lower',cmap=None)
    py.show()
    return None    