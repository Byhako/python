"""

Indicador 	Modo de apertura 	Ubicación del puntero

r 	Solo lectura 	Al inicio del archivo

rb 	Solo lectura en modo binario 	Al inicio del archivo

r+ 	Lectura y escritura 	Al inicio del archivo

rb+ 	Lectura y escritura en modo binario 	Al inicio del archivo

w 	Solo escritura. Sobreescribe el archivo si existe.
        Crea el archivo si no existe 	Al inicio del archivo

wb 	Solo escritura en modo binario. Sobreescribe el archivo si existe.
        Crea el archivo si no existe 	Al inicio del archivo

w+ 	Escritura y lectura. Sobreescribe el archivo si existe.
        Crea el archivo si no existe 	Al inicio del archivo

wb+ 	Escritura y lectura en modo binario. Sobreescribe el archivo si existe.
        Crea el archivo si no existe 	Al inicio del archivo

a 	Añadido (agregar contenido). Crea el archivo si éste no existe
  	Si el archivo existe, al final Si no existe, al comienzo

ab 	Añadido en modo binario (agregar contenido).
        Crea el archivo si éste no existe 	Si el archivo existe, al
                            final de éste. Si el archivo no existe, al comienzo

a+ 	Añadido (agregar contenido) y lectura. Crea el archivo si éste no
        existe.  	Si el archivo existe, al final de éste.
                         Si el archivo no existe, al comienzo

ab+ 	Añadido (agregar contenido) y lectura en modo binario.
         Crea el archivo si éste no existe
"""


# seek(byte) Mueve el puntero hacia el byte indicado.

archivo = open("ejemplo.dat", "r")
contenido = archivo.read()
# el puntero queda al final del documento
#archivo.seek(0)
archivo.close()
# read([bytes]) Lee todo el contenido de un archivo. Si se le pasa la longitud
# de bytes, leera solo el contenido hasta la longitud indicada.


archivo = open("ejemplo.dat", "r")
contenido = archivo.read()
print('read() \n%s \n' %(contenido))
archivo.close()


# readline([bytes]) Lee una linea del archivo.


archivo = open("ejemplo.dat", "r")
linea1 = archivo.readline()
print('readline() %s \n' %(linea1))
archivo.close()


# readlines() Lee todas las lineas de un archivo.


archivo = open("ejemplo.dat", "r")
print('readlines(): \n')
for linea in archivo.readlines():
    print('linea: %s' %(linea))
print('\n')
archivo.close()


# tell() Retorna la posicion actual del puntero.


archivo = open("ejemplo.dat", "r")
linea1 = archivo.readline()
mas = archivo.tell()
print('tell() %i\n' %(mas))
archivo.close()


# write(cadena) Escribe cadena dentro del archivo.

archivo = open("ejemplo.dat", "a")
archivo.write('56\n')
archivo.close()

archivo = open("ejemplo.dat", "r")
contenido = archivo.read()

print(contenido)
print('write() $i \n' %(contenido))
archivo.close()


# writelines(secuencia) Secuencia sera cualquier iterable cuyos
# elementos seran escritos uno por línea.

archivo = open("ejemplo.dat", "a")
lista = ['Linea 1\n', 'Linea 2']
archivo.writelines(lista)
archivo.close()

archivo = open("ejemplo.dat", "r")
contenido = archivo.read()

print(contenido)
#print('write() $s \n' %(contenido))
archivo.close()