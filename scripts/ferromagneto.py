import numpy as np
import time
ini=time.time()

red=100
kb=1.0

##Condicion de frontera periodica
def cf(x):
    if x+1>red-1:
        return 0
    elif x-1<0:
        return red-1
    else:
        return x
        
##Estado inicial
def inicio():
    spin=np.random.random_integers(0,1,(red,red))
    spin[spin==0]==-1
    return spin
 
##Energia
def energia(spin,i,j):
    a1=cf(j-1)
    a2=cf(j+1)
    a3=cf(i-1)
    a4=cf(i+1)
    a=spin[i,a1]+spin[i,a2]+spin[a3,j]+spin[a4,j]
    return -1*spin[i,j] *(a)-spin[i,j]*H 

##sumo elementos de matriz
def suma(m):
    sum=0
    for i in range(red):
        for j in range(red):
            sum=sum+m[i,j]
    return sum   
     
##Algoritmo de metropolis
def met(T):
    spin=inicio()
    
    b=1/(T*kb)
    for i in range(red):
        for j in range(red):
            
            delta=-2.0*energia(spin,i,j)
        
            if delta<=0:
                spin[i,j]*=-1
            elif np.exp(-b*delta)>=np.random.random():
                spin[i,j]*=-1
    
    return spin


##    
escriba=open("ferro70.dat", 'w') #abre archivo
T=70.0
 
for H in np.arange(-30,30,0.1):
    ban=0
    for paso in range(150):
        matriz=met(T)
        Mj=suma(matriz)
        ban=ban+Mj
    M=ban/150.0
    print(H,M,Mj)   
    escriba.write('%3.5f     %3.5f\n' %(H,M))
    
escriba.close()    

fin=time.time()

print('Tiempo de ejecucion: %2.2f segundos' %(fin-ini))     

"""
Programa para modelar la magnetizacion contra el campo magnetico
de un ferromagneto tipo ISING
20/11/2015
"""           