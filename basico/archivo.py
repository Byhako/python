from os import path

#=====================================
#                 LEER
#=====================================
# scp edison@c3.itm.edu.co:/home/edison/Ruben/working/area/tiempo_sucursal.py /home/ruben/Documentos/
# scp /home/ruben/Documentos/working/area/3customer.py  edison@c3.itm.edu.co:/home/edison/Ruben/working/area
# ***** VECTORES CON LOS DATOS DE COLUMNAS *****

x = []
y = []
archivo = open('dato.dat', 'r')

for line in archivo:
    line = line.split()
    x.append(eval(line[0]))
    y.append(eval(line[1]))

archivo.close()


# ***** METODO READ *****
# El metodo read devuelve una cadena con el contenido del archivo o bien el
# contenido de los primeros n bytes, si se especifica el tamano maximo a leer.

archiv = open('dato.dat','r')
completo = archiv.read(128)
print(completo,'\n')
archiv.close()

with open('dato.dat') as file:
  print(file.read())

# ***** COMO LISTA LEE POR FILAS *****

archiv = open('dato.dat','r')
while True:
      linea = archiv.readline()
      if not linea: break
      x.append(linea)

archiv.close()

# ******** METODO seek(byte) ****************
# Mueve el puntero hacia el byte indicado.
# seek(a,b) se mueve a bytes desde posicion b. 
# b=0 inicio, b=1 actual, b=2 final

archivo = open("ejemplo.dat", "r")
contenido = archivo.read()
# el puntero queda al final del documento
archivo.seek(0)  # regresa al inicio
archivo.close()


# ****** METODO tell() **********
#Retorna la posicion actual del puntero.

archivo = open("ejemplo.dat", "r")
linea1 = archivo.readline()
mas = archivo.tell()
print('tell() %i\n' %(mas))
archivo.close()


#=====================================
#                GENERAR
#=====================================

escriba = open("nombre.dat", 'w')

for i in range(0,10):
  b = 2*i
  a = i
  escriba.write('%5s %5s\n' %(a,b))

escriba.close()

# ***** VARIOS ARCHIVOS *****

l = 10

for i in range (l):
  escriba = open("onda"+str(i)+".dat", 'w')

  for j in range(9):
    y = j + i
    z = j - i
    escriba.write('%s        %s\n\n' %(str(y),str(z)))
  escriba.close()

# writelines(secuencia) Secuencia sera cualquier iterable cuyos
# elementos seran escritos uno por línea.

archivo = open("ejemplo.dat", "a")
lista = ['Linea 1\n', 'Linea 2']
archivo.writelines(lista)
archivo.close()

# para escribir sin esperar a que se cierre el archivo flush()

#=====================================
#              COMPRESION
#=====================================

# ************ ZIP ************
import zipfile

with zipfile.ZipFile('comprimido.zip', 'w') as f
  fzip.write('albun.json')
  fzip.write('albun.xml')
  fzip.write('empleados.csv')

fzip = zipfile.ZipFile('comprimido.zip')
fzip.printdir()  # info
fzip.namelist()  # lista con nombres de ficheros.

info = fzip.infolist()
for i in info:
  print(i.filename, i.date_time, i.compress_size, i.filemode)

fzip.extractall(path="/home/ruben/", pwd='password')




# ************ GZIP ************
import gzip

with open('fic.dat', 'rb') as archivo:
  with gzip.open('fichero.txt.gz', 'wb') as fich:
    fich.writelines(archivo)

datos_binarios = b'cadena binaria'
with gzip.open('nuevo.gz', 'wb') as fich:
  fich.write(datos_binarios)

comprimidos = gzip.compress(datos_binarios)



# ************ TAR ************
import tarfile
ftar = tarfile.open('fichero.tar.gz', 'w:gz')
ftar.add('arichivo.dat')
ftar.add('carpeta')
ftar.close()

ftar = tarfile.open('fichero.tar.gz', 'r:gz')
ftar.extractall()
ftar.close()

ftar.list()
ftar.getnames()



#=====================================
#                FORMATOS
#=====================================

# ************ CSV ************
# import csv


with open('empleados.csv') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    print(row[0] ,row[1], row[2], row[3])


fich = open('nuevo.csv', 'w')
fw = csv.writer(fich, delimiter=';')
lista = [[1,2,3],[4,5,6]]
for fila in lista:
  fw.writerow(fila)

fich.close()

# ************ XML ************
# from xml.etree.ElementTree import parse

doc = parse('albun.xml')
for ele in doc.findall('titulo'):
  print(ele.text)

# from xml.dom.minidom import parse, Node

tree = parse('albun.xml')
for nodo in tree.getElementsByTagName('titulo'):
  for nodo_hijo in nodo.childNodes:
    if nodo_hijo.nodeType == Node.TEXT_NODE:
      print(nodo_hijo.data)

# import xml.sax.handler
# import xml.sax

class Albunsax(xml.sax.handler.ContentHandler):

  def __init__(self):
    self.in_title = False

  def startElement(self, name, atributos):
    if name =='titulo':
      self.in_title = True

  def caracter(self, data):
    if self.in_title:
      print(data)

  def endElement(self, name):
    if name =='titulo':
      self.in_title = False


parser = xml.sax.make_parser()
sax_handler = Albunsax()
parser.setContentHandler(sax_handler)
parser.parse('albun.xml')



# ************ JSON ************

# import json

fich = open("albun.json")
line = fich.readline()
fich.close()
data = json.loads(line) # diccionario

data["albun"]["tirulos"].append("fuego")
cad = json.dumps(data)
new = open('new.json','w')
new.writeline(cad)
new.close()


#///////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////

# para obtener el path correcto independiente del 
# sistema operativo en el que trabajemos: (importar path)

ruta = path.join('fichero1' , 'fichero2', 'archivo.txt')
# fichero1/fichero2/archivo.txt

# la variable sep nos da el separador que usa el OS. veamos.
sep.join('ss')[1]

# ***** SERIALIZACION ***********
# import pickle

cadena = 'me gusta programar 7 veces en semana'

with open('escribe.bin','wb') as f:
  pickle.dump(cadena,f)

# deserializar

with open('escribe.bin','rb') as f:
  cad = pickle.dump(f)

print(cad)

"""
 import numpy as np

 datos=np.zeros((3,2),float)

 datos[:,0]=1.0
 datos[:,1]=2.0
 print(datos)

np.savetxt('archivo.dat',datos)

 new=np.loadtxt('archivo.dat')

 m=np.size(new)
 f=len(new[:,0])
 c=int(m/f)

print('la matriz tiene %s filas y %s columnas' %(f,c))



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