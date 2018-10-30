import numpy as np

def f(x):
  return x**3 + (15*x**4)/4

def romberg(a,b,n):
  h = (b - a)/n
  if(n==1):
    return (h/2)*(f(a) + f(b))
  else:
    s = 0
    print(a,'     ',f(a))
    for i in range(1,n):
      s += f(a + i*h)
      print(a + i*h,'     ',f(a + i*h))
    
    print(b,'     ',f(b))
    print('h/2 = ',h/2)
    return (h/2)*(f(a) + 2*s + f(b))

print(romberg(0,1,50))