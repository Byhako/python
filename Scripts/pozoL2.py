import numpy as np
import time

inicio=time.time()

##================================================================
def fu(E,h,v0):
    
    y1=np.sqrt(E/(v0-E))*np.cos((np.pi/2.0) + np.sqrt(v0-E)*h/2.0)
    y2=np.sin((np.pi/2.0) + np.sqrt(v0-E)*h/2.0)
    y=y2-y1
    return y


def ceros(h):    #biseccion
    #escojo 1 intervalo
    for x1 in range(5,100):
        x2=x1+1.0
        y1=fu(x1,h,v0)
        y2=fu(x2,h,v0)
        if y1*y2<0.0: break
    
    #escojo 2 intervalo
    for x3 in range(int(x2),100):
        x4=x3+1.0
        y3=fu(x3,h,v0)
        y4=fu(x4,h,v0)
        if y3*y4<0.0: break
        
    #escojo 3 intervalo
    for x5 in range(int(x4),100):
        x6=x5+1.0
        y5=fu(x5,h,v0)
        y6=fu(x6,h,v0)
        if y5*y6<0.0: break
    
        
    for i in range(10):
        xm=(x1+x2)/2.0
        if fu(xm,h,v0)==0.0: break
        if fu(x1,h,v0)*fu(xm,h,v0)<0.0:
            x2=xm
        if fu(x2,h,v0)*fu(xm,h,v0)<0.0:
            x1=xm
      
    if fu(x1,h,v0)*fu(x2,h,v0)>0:
        print('El metodo fallo')
    
    cero1=(x1+x2)/2.0
##
    for i in range(10):
        xm=(x3+x4)/2.0
        if fu(xm,h,v0)==0.0: break
        if fu(x3,h,v0)*fu(xm,h,v0)<0.0:
            x4=xm
        if fu(x4,h,v0)*fu(xm,h,v0)<0.0:
            x3=xm
      
    if fu(x3,h,v0)*fu(x4,h,v0)>0:
        print('El metodo fallo')
    
    cero2=(x3+x4)/2.0      
##
    for i in range(10):
        xm=(x5+x6)/2.0
        if fu(xm,h,v0)==0.0: break
        if fu(x5,h,v0)*fu(xm,h,v0)<0.0:
            x6=xm
        if fu(x6,h,v0)*fu(xm,h,v0)<0.0:
            x5=xm
      
    if fu(x5,h,v0)*fu(x6,h,v0)>0:
        print('El metodo fallo')
    
    cero3=(x5+x6)/2.0      
 
    return cero1,cero2,cero3

##================================================================


escriba=open('pozo2.dat', 'w')

#xme: masa efectiva de electron en GaAs
#cdL: Constante dielectrica del GaAs
xme = 0.0665
cdL = 12.35
#a0: effective Bohr radius in Amstrongs
#ry: effective Rydberg in meV
a0=cdL*0.529177/xme
ry=13.6058*xme/(cdL**2)*1000.0


v0=43.1864
for a in np.arange(5,15,1):
    en1,en2,en3=ceros(a)
    
    escriba.write('%4.4f       %4.4f       %4.4f       %4.4f\n' %(a,en1,en2,en3))
        
escriba.close()    

#*********************************************************




fin=time.time()
print('Tiempo de ejecucion: %4.1f segundos' %(fin-inicio))
"""
Pozo cuadrado unidimensional finito para energias
pares, en funcion del ancho del pozo para una
profundidad (potencial) constante
\Dropbox\personal\pozo
"""