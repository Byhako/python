"""
METODO DE JACOBI (GAUSS-SEIDEL) para resolver sistemas 3 x 3
de la forma Ab = x

Ruben E Acosta.

2016-02-27
"""
from numpy import *
import numpy as np

def jacobi(A,b):
    """
    A -> matriz
    b -> vector
    """
    ciclos=0
    convergencia=1
    n=len(b)
    xa=zeros(n)
    while (convergencia>0.01):
        for i in range(n):
            s=0
            for j in range(n):
                if j!=i:
                    s=s+A[i,j]*xa[j]
        
            xi=(b[i]-s)/A[i,i]
            xa[i]=xi
        
        X=matrix(xa).getT()  #verificamos precision
        B=matrix(b).getT()
        c=A*X-B
        convergencia=0
        for i in range(n):
            convergencia=convergencia+abs(c[i,0])
        ciclos=ciclos+1
        if ciclos>20:
            print('El metodo diverge')
            print(convergencia)
            #xa=0 
            break
    return(xa)      
    
A = np.matrix([[5,-8,3],[-2,6,-9],[3,-5,2]])
b = np.matrix([[-71],[134],[-58]])

x=jacobi(A,b)
print(x) 
"""
Si la matriz tiene elementos cero en la diagonal, el metodo falla
por diviciones cero.
""" 
    