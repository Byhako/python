import numpy as np

def f(x):
  return -3*x*x+5

def df (x,h): 
  return (1/(2*h))*(f(x+h) - f(x-h))

x = 2
h = 0.01

print(f(x+h))
print(f(x-h))
print(df(x,h))