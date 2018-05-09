import numpy as np

def f(x):
  return np.exp(x)*(x**3)

def df (x,h): 
  return (1/(2*h))*(f(x+h) - f(x-h))

x = 0.3
h = 0.01

print(f(x+h))
print(f(x-h))
print(df(x,h))