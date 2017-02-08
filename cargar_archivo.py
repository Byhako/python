# -*- coding: cp1252 -*-

# __init__.py  para que una carpeta pueda ser considerada un paquete


from pylab import *
from numpy import *

#=======================
#       LEER
#=======================

# ***** VECTORES CON LOS DATOS DE COLUMNAS *****

x = []
y = []
archivo = open('1_0.dat', 'r')  # abre archivo para leer

for line in archivo:
    line = line.split()  # convierte linea en vertor
    x.append(eval(line[0])) #vertor x, valores col(1)
    y.append(eval(line[1])) #vertor y, valores col(2)

archivo.close()

print x  #imprimo primera columna como un vector
print''
plot(x,y)
#show()

# ***** LEE POR FILAS *****

archivo=open('1_0.dat','r') #abre archivo para leer
for i in range(0,2):
        linea=archivo.readline()
        print linea  #imprimo 2 primera filas
archivo.close()
print''

# ***** METODO READ *****

archiv=open('1_0.dat','r')
# El metodo read devuelve una cadena con el contenido del archivo o bien el
# contenido de los primeros n bytes, si se especifica el tamano maximo a leer.
completo=archiv.read(128)
print completo
print''
archiv.close()

# ***** COMO LISTA *****

archiv=open('1_0.dat','r')
while True:
      linea=archiv.readline()
      if not linea: break
      x.append(linea)  #carga los datos en x como una lista

archiv.close()


#=======================
#       GENERAR
#=======================
escriba=open("nombre.dat", 'w') #abre archivo en disco para escribir. w = write


for i in range(0,10):
      b=2*i
      a=i
      escriba.write('%5s %5s\n' %(a,b))  #suma parejas y escribe con formato

escriba.close()

#varios archivos
l=10

for i in range (l):
    escriba=open("onda"+str(i)+".dat", 'w') #abre archivo

    for j in range(9):
        y=j+i
        z=j-i
        escriba.write('%s        %s\n\n' %(str(y),str(z)))
    escriba.close()


# import numpy as np
#
# datos=np.zeros((3,2),float)
#
# datos[:,0]=1.0
# datos[:,1]=2.0
# print(datos)
#
# np.savetxt('archivo.dat',datos)
#
# new=np.loadtxt('archivo.dat')
#
# m=np.size(new)
# f=len(new[:,0])
# c=int(m/f)
#
# print('la matriz tiene %s filas y %s columnas' %(f,c))
#
