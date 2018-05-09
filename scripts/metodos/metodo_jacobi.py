import numpy as np

def jacobi(A, b, x0):
  x = np.matrix([[0.0],[0.0],[0.0]])
  n = A.shape[0]
  k = 1

  while True:
    for i in range(n):
      s = 0.0
      for j in range(n):
        if(j!=i):
          s = s + A[i,j]*x0[j]      
      x[i] = (b[i] - s)/A[i,i]

    x0 = x
    print('\nIteracion ',k)
    print('x:\n',x)
    k = k + 1
    error = np.linalg.norm( A*x - b )
    print('\nError: ',error)
    if(error<0.01):
      break
    if k>10:
      print('No converge.')
      break
    
  return x0

A = np.matrix([[1,70,-3],[30,-1,-2],[3,-2,-100]])
b = np.matrix([[-193],[78.5],[714]])
x0 = np.matrix([[0.0],[0.0],[0.0]])

x = jacobi(A, b, x0)

print('\nVector aproximado:\n',x)