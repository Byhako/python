import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return (np.exp(x))/(x-1)

def simpson(a,b,n):
  h = (b-a)/n
  x = np.linspace(a,b,n+1)

  s1 = 0
  s2 = 0
  print(x[0],'   ', f(x[0]))

  for i in range(1,int(n/2 - 1)+1):
    s1 = s1 + f(x[2*i])
    print(x[2*i],'   ', f(x[2*i]))
  
  for i in range(1,int(n/2)+1):
    s2 = s2 + f(x[2*i-1])
    print(x[2*i-1],'   ', f(x[2*i-1]))

  print(x[-1],'   ', f(x[-1]))

  return (h/3)*( f(x[0]) + 2*s1 + 4*s2 + f(x[-1]) )

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

plt.ylim(0,1.1*y1[-1])
plt.xticks(np.linspace(a,b,n+1),np.linspace(a,b,n+1))

print(simpson(a,b,n))
plt.show()