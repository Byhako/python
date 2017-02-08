import random


print('ESTIMAR PI EN UN CIRCULO UNIDAD')
print('')

#MUESTREO SIMPLE

n=0
m=10000
c=0
c1=0

while c<m:
    c1=c1+1
    x=random.random()
    y=random.random()
    if x**2+y**2<1:
        n=n+1
    else:
        c=c+1

print('Muestreo simple = %3.4f' %(4*n/c1 ))   

#MARKOV

n=0     #asiertos
m=10000 #intentos
x=0
y=0
c=0 
c1=0
p=0.3  #paso
while c<m:
    c1=c1+1
    dx=random.uniform(-p,p)
    dy=random.uniform(-p,p)
    if (abs(x+dx)<1 and abs(y+dy)<1):
        x=x+dx
        y=y+dy
    else:
        if x**2+y**2<1:
            n=n+1
        else:
            c=c+1        
       
print('Marcov = %3.4f' %(4*n/m))   
"""
El algoritmo comienza a partir de una posición dada en el espacio a ser muestreados [aquí (0, 0)] y genera la posición del nuevo punto desde la posición de la anterior. Si la nueva posición se encuentra fuera de la plaza, se rechaza (línea 38). Una selección cuidadosa del tamaño de paso p utiliza para generar números aleatorios en el intervalo [-p, p] es de importancia: cuando p es demasiado pequeño, la convergencia es lenta, mientras que si p es demasiado grande muchos movimientos son rechazados porque la simulación menudo dejar el cuadrado unitario. Por lo tanto, un valor de p tiene que ser seleccionado de tal manera que se aceptan movimientos consecutivos aproximadamente el 50% del tiempo.
"""     
