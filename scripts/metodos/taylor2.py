# Metodo de taylor orden 2 para problemas de valor inicial
import numpy as np

# y' = f(x,y)
def f(x,y):
  return np.cos(x*y)

# y'' = f'(x,y) = F(x,y)
def F(x,y):
  return -(x*np.cos(x*y) + y)*np.sin(x*y)

def taylor(x0, xf, y0, n):
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
    yn = y[i] + h*f(x[i],y[i]) + h*h*F(x[i],y[i])/2
    y.append(yn)
    print(x[i],'    ',y[i])

  print('\n',x[-1],'    ',y[-1])
  return y

taylor(0, 1, 1, 2)