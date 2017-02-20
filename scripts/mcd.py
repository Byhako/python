import time
inicio=time.time()
a=60
b=48

for i in range(min(a,b),1,-1):
        if a%i==0 and b%i==0:
                print('El maximo comun divisor de %s y %s es %s:' %(a,b,i))
                break
else:
        print('Los numeros %s y %s son primos entre si.' %(a,b))

fin=time.time()
print('Tiempo de ejecucion: ', fin-inicio) 