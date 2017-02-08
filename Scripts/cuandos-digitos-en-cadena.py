"""
Dada una cadeda, digo cuantos digitos posee.

Ruben E Acosta

2016-02-27
"""

from pylab import *

cadena='2,21,4,22a2a,1'
con=0
con2=0
con3=0
di=0
for i in cadena:
      con=con+1
      b=ord(i) #codigo ASCII del caracter
               
      if (b<58) and (b>47):   # verifico si es numero
            con2=con2+1
            con3=0
      else:
            con3=2
                        
      if con2==1 and con3>0:    #si es digito sumo 1
            di=di+1
            con2=0
            con3=0

      if con3>0:
            con2=0
            
a=cadena[len(cadena)-1]
b=ord(a)

if (b<58 or b>47):  #verifico si ultimo caracter es numero
      di=di+1

print(di)
