

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

# ******** METODO seek(byte) Mueve el puntero hacia el byte indicado.

archivo = open("ejemplo.dat", "r")
contenido = archivo.read()
# el puntero queda al final del documento
archivo.seek(0)  # regresa al inicio
archivo.close()

# ****** METODO tell() Retorna la posicion actual del puntero.

archivo = open("ejemplo.dat", "r")
linea1 = archivo.readline()
mas = archivo.tell()
print('tell() %i\n' %(mas))
archivo.close()




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

# writelines(secuencia) Secuencia sera cualquier iterable cuyos
# elementos seran escritos uno por línea.

archivo = open("ejemplo.dat", "a")
lista = ['Linea 1\n', 'Linea 2']
archivo.writelines(lista)
archivo.close()


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


"""

Indicador   Modo de apertura  Ubicación del puntero

r   Solo lectura  Al inicio del archivo

rb  Solo lectura en modo binario  Al inicio del archivo

r+  Lectura y escritura   Al inicio del archivo

rb+   Lectura y escritura en modo binario   Al inicio del archivo

w   Solo escritura. Sobreescribe el archivo si existe.
        Crea el archivo si no existe  Al inicio del archivo

wb  Solo escritura en modo binario. Sobreescribe el archivo si existe.
        Crea el archivo si no existe  Al inicio del archivo

w+  Escritura y lectura. Sobreescribe el archivo si existe.
        Crea el archivo si no existe  Al inicio del archivo

wb+   Escritura y lectura en modo binario. Sobreescribe el archivo si existe.
        Crea el archivo si no existe  Al inicio del archivo

a   Añadido (agregar contenido). Crea el archivo si éste no existe
    Si el archivo existe, agrega al final, Si no existe, al comienzo

ab  Añadido en modo binario (agregar contenido).
        Crea el archivo si éste no existe   Si el archivo existe, al
                            final de éste. Si el archivo no existe, al comienzo

a+  Añadido (agregar contenido) y lectura. Crea el archivo si éste no
        existe.   Si el archivo existe, al final de éste.
                         Si el archivo no existe, al comienzo

ab+   Añadido (agregar contenido) y lectura en modo binario.
         Crea el archivo si éste no existe
"""