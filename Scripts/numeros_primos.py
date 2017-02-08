import math
from time import time 
inicio=time()
print('%1s\n' %('NUMEROS PRIMOS'))

"""
Teorema de wilson:
si p es primo cumple:
(p-1)!=-1(mod(p))

podemos escribir esto como:

(p-1)! % p=p-1
"""
#generamos los Z primeros primos 
Z=10
primos=[]
a=1
p=1
while a<Z+1:
    p=p+1
    s=0
    for i in range(2,p):
        b=p%i
        if b==0:
            s=1
            break
    if s==0:
        primos.append(p)
        a=a+1
       
print('Los %1s primeros primos son: %1s\n' %(Z,primos)) 

#///////////////////////////////////////////
# Criba de Eratostenes
def primos(x):

  n = [i for i in range(2,x+1)]
  Uprimo = n[0]
  i = Uprimo
  con = 0

  while Uprimo**2 <= x:

    while i<=x:  # elimino multiplos del primo
      i += Uprimo
      n.remove(i)

    con += 1
    Uprimo = n[con]

  return n
#////////////////////////////////////
def es_primo(x):
    s=0
    if x==0 or x==1 or x<0:s=1
    for i in range(2,x//2):
        a=x%i
        if a==0:
            s=1
            break
    if s==0: return True
    if s==1: return False
    
print(es_primo(5))
#////////////////////////////////////

# """
# Postulado de Bertrand:
# 
# Si n es un número natural mayor que 3, entonces siempre existe
# un número primo p tal que n < p < 2n- 2.
# """
# 
# #Hallamos cota superio.
# nmax=int(floor(((primos[Z-1])+2)/2))
#  
# for i in range(4,nmax+1):
#     p=[]
#     n1=i
#     n2=2*i-2
#     for i in range(Z):
#         if n1<primos[i] and primos[i]<n2:
#             p.append(primos[i])
#     print('En el intervalo (%1s %1s) estan los primos:' %(n1,n2))
#     print('%s\n' %(p))

#======================================
# FUNCION QUE SACA FACTORIES PRIMOS
#======================================
def primos(n):
      x=[]
      a=int(n)

      while (a%2)==0: # Comprobamos si 2 es factor de a      
            x.append(2)
            a=a/2
	
      #Probamos el resto de impares solo hasta la raiz cuadrada de a
      c=3

      while c<=math.sqrt(a) and a>1:
            if (a%c)==0:
                  x.append(c)
                  a=a/c
            else:
                  c=c+2
      if a>=1:
            x.append(a)

      return x	
      
#======================================
fin=time()
print('Tiempo de ejecucion: ', fin-inicio)            