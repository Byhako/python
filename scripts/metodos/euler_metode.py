# Metodo de Euler para problemas de valor inicial

import numpy as np

# y' = F(x,y)
def F(x,y):
  return x + y

def euler(x0, xf, y0, n):
  """
  x0 = punto inicial
  xf = punto objetivo
  y0 = valor inicial
  n = numero de pasos
  """
  h = (xf - x0)/n
  print('h = ',h,'\n')

  x = np.linspace(x0,xf,n+1)
  y = [y0]
  for i in range(n):
    yn = y[i] + h*F(x[i],y[i])
    y.append(yn)
    print(x[i],'    ',y[i])

  print('\n',x[-1],'    ',y[-1])
  return y

euler(0,0.2,0,4)