import numpy as np

def seidel(A, b, x0):
  x1 = np.matrix([[0.0],[0.0],[0.0]])
  n = A.shape[0]
  k = 1
  while True:
    for i in range(n):
      s1 = 0.0
      s2 = 0.0
      for j in range(n):
        if(j<i-1):
          s1 = s1 + A[i,j]*x1[j]
        if(i+1<=j):
          s2 = s2 + A[i,j]*x0[j]

      x1[i] = (b[i] - s1 - s2)/A[i,i]

    x0 = x1

    print('\nIteracion ',k)
    print('x:\n',x1)
    k = k + 1
    error = np.linalg.norm( A*x1 - b )
    print('\nError: ',error)
    if(error<0.01):
      break
    if k>10:
      print('No converge.')
      break
    
  return x0

A = np.matrix([[1,70,-3],[30,-1,-2],[3,-2,-100]])
b = np.matrix([[-193],[78.5],[714]])
x0 = np.matrix([[2.0],[-3.0],[-7.0]])

x = seidel(A, b, x0)

print('\nVector aproximado:\n',x)