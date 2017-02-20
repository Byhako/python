"""
De decimal a binario y equivalencia hasta 16

Ruben E Acosta

2016-02-27
"""
from numpy import *

def bin(x):
      x=long(x)
      l=['000','001','010','011','100','101','110','111']
      return ''.join([l[int(c)] for c in "%o"%x])

for k in range(17):
      y=bin(k)
      t=k
      print(t,'=',y)

print('')
print(bin(889))
