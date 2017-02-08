"""
Derivada por diferencias finitas centrales.

Ruben E Acosta

2016-02-27
"""
import numpy as np

def f(x):
	f=(x)**2
	return f

h=1e-5
x=2
#Primera
f1=(f(x+h)-f(x-h))/(2*h)
#Segunda
f2=(f(x+h)-2*f(x)+f(x-h))/(h*h)
#Tercera
f3=(f(x+2*h)-2*f(x+h)+2*f(x-h)-f(x-2*h))/(2*h**3)

print('Primera: %4.4f'%(f1))
print('Segunda: %4.4f'%(f2))
print('Tercera: %4.4f'%(f3))
