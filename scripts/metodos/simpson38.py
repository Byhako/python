import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.exp(x**3) 

def simpson(a,b,n):
  h = (b-a)/n
  x = np.linspace(a,b,n+1)

  s1 = 0
  s2 = 0
  s3 = 0

  print(x[0],'   ', f(x[0]))

  for i in range(1,int(n-2)+1,3):
    s1 = s1 + f(x[i])
    print(x[i],'   ', f(x[i]))
  
  for i in range(2,int(n-1)+1,3):
    s2 = s2 + f(x[i])
    print(x[i],'   ', f(x[i]))

  for i in range(3,int(n-3)+1,3):
    s3 = s3 + f(x[i])
    print(x[i],'   ', f(x[i]))
  
  print(x[-1],'   ', f(x[-1]))
  
  return (3*h/8)*( f(x[0]) + 3*s1 + 3*s2 + 2*s3 + f(x[-1]) )

a = 1
b = 3
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