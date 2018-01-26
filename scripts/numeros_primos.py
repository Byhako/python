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
<<<<<<< HEAD
  p=p+1
  s=0
  for i in range(2,p):
    b = p%i
    if b == 0:
      s = 1
      break
  if s==0:
     primos.append(p)
     a=a+1
       
print('Los %1s primeros primos son: %1s\n' %(Z,primos)) 
=======
    p = p+1
    s = 0
    for i in range(2,p):
        b = p%i
        if b==0:
            s = 1
            break
    if s==0:
        primos.append(p)
        a=a+1

print('Los %1s primeros primos son: %1s\n' %(Z,primos))
>>>>>>> 413d59534a309cacf0a3a03fd7eda221cc0989ab

#///////////////////////////////////////////
# Criba de Eratostenes
def primos(x):
  n = [0 for i in range(x+1)]
  index = 2

  while index**2<=x:
    aux = 2*index
    if n[index]==1:
      index += 1
      continue
    while aux<=x:
      n[aux] = 1
      aux += index

    index += 1

    p = []
    for i in range(x+1):
      if n[i]==0:
        p.append(i)

  return p

print(primos(100))

#///////////////////////////////////////////
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
#///////////////////////////////////////////

fin=time()
print('Tiempo de ejecucion: ', fin-inicio)


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
