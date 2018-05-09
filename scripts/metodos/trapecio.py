import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return (x**(3/2))*(np.exp(2*x))

def trapecio(a,b,n):
  s1 = (f(a) + f(b))/2.0
  print('s1',s1)
  s2 = 0
  for k in range(1,n):
    s2 = s2 + f(a + k*((b-a)/n))
    print(f(a + k*((b-a)/n)))

  return ((b-a)/n)*(s1 + s2)

a = 2
b = 4
n = 4

x1 = np.linspace(a,b,n+1)
x2 = np.linspace(a,b,50)
y1 = f(x1)
y2 = f(x2)

plt.plot(x2,y2, linewidth=3.0)

for i in range(n+1):
  plt.plot([x1[i],x1[i]],[0,y1[i]], 'k-', linewidth=1)

plt.plot(x1,y1, 'r-o', linewidth=1.2)
plt.ylim(0,1.1*y1[-1])

print(trapecio(a,b,n))
plt.show()