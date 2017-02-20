import math
import time
inicio=time.time()

z=100  #numero de cifras

def combinar(listas):
    resultados=[]
    for numeros in listas:
        for i in numeros:
            resultados.append(i)
    return resultados

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

vp=[] #vector de factores primos 
for i in range(1,z+1):
      yi=[]
      yi=primos(i)  # uso funcion primos definida antes
      vp.append(yi)

#hayo numero mas grande en vp
cad=combinar(vp)
cad.sort()
lim=cad[len(cad)-1]
fac=[]
#genero lista fac
for numero in range(1,lim+1):
      s2=0
      for unidad in vp:
            s1=0
            for elemento in unidad:
                  if elemento==numero:s1+=1
            if s1>s2:s2=s1
      for i in range(s2):
            fac.append(numero)            
                              
mcm=1
for i in range(len(fac)):
      mcm=mcm*fac[i]
      
print ('El numero mas pequeño que puede ser dividido enteramente por todos los naturales entre 1 y %d es %d' %(z,mcm))

fin=time.time()
print('Tiempo de ejecucion: %6f' %(fin-inicio))   

"""
hacemos un vector con todos los factores primos de los digitos entre 1 y z
1  [1]
2  [2]
3  [3]
4  [2,2]
5  [2,5]
6  [2,3]
7  [7]
8  [2,2,2]
... etc ...


luego vemos cuantas veces esta un numero primo dado como factor de cada digito y la mayor cantidad de veces la guardamos
en el vector llamado 'fac' para el ejemplo seria fac=[2,2,2,3,5,7].  solo tomamos 3 veces el dos, ya que 3 es la
maxima cantidad de veces que esta como factor para un numero (en 8).

ahora multiplicamos las entradas de fac, y listo!!!
"""










      
