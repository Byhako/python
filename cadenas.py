from operator import itemgetter
import re

# ///////////////////////////////////////////////////
# ********************  FORMATO  ********************
# ///////////////////////////////////////////////////

# Letra capital

cadena = "bienvenido a mi aplicacion"
print(cadena.capitalize())

# Cadena a minuscula

cadena = "Hola Mundo"
print(cadena.lower())

# Cadena a mayuscula

cadena = "Hola Mundo"
print(cadena.upper())

# Invierte mayusculas y minusculas

cadena = "Hola Mundo"
print(cadena.swapcase())

# Formato de titulo

cadena = "hola mundo"
print(cadena.title(), '\n')

# Centrar un texto center(longitud[, "caracter de relleno"])

cadena = "bienvenido a mi aplicacion".capitalize()
print(cadena.center(50, "="), '\n')
print(cadena.center(50, " "), '\n')

# Alinear texto a la izquierda ljust(longitud[, "caracter de relleno"])

cadena = "bienvenido a mi aplicacion".capitalize()
print(cadena.ljust(50, "="), '\n')

# Alinear texto a la derecha rjust(longitud[, "caracter de relleno"])

cadena = "bienvenido a mi aplicacion".capitalize()
print(cadena.rjust(50, "="), '\n')

# Cadena rellena con 0 a la iz hasta alcanzar longitud indicada.

numero_factura = 1575
print(str(numero_factura).zfill(12), '\n')

# ordenar.
# ordenapor letra
lista = [('a',2),('c',2),('b',3),('d',3),('z',1),('a',1),('d',1),('e',4)]
m = sorted(lista, key=itemgetter(0,1))

# ordenar por numero
m = sorted(lista, key=itemgetter(1,0))


# ///////////////////////////////////////////////////
# ********************  BUSQUEDA ********************
# ///////////////////////////////////////////////////


# Contar cantidad de apariciones de una subcadena
# count("subcadena" [, posicion_inicio, posicion_fin])

cadena = "bienvenido a mi aplicacion".capitalize()
print('Cuento en cadena %i \n' %(cadena.count("a")))

# Buscar una subcadena dentro de una cadena
# find("subcadena" [posicion_inicio, posicion_fin])
# Retorna posición donde inicia subcadena. Si no la encuentra, retorna -1.

cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.find("mi"))
print(cadena.find("mi", 0, 10), '\n')

# Buscar y extraer elemento si lo encuentra, si no, retorna
# None

m = re.search(r'\d\d\d', 'hola789adios').group()
print(m)

# Buscar cadenas complejas.
# buscar y agrupar en dos grupos, uno para numeros hasta el guion, 
# y otro para las letras que siguen.

regex = re.compile(r'(\d+)-([A-Za-z]+)')
m = regex.search('ams12357-mono')
print('numeros %s  letras %s\n' % (m.group(1), m.group(2)))

# Busca todas las coincidencias y regresa tupla de los que 
# cumplen el patron

m = re.findall(r'\d{3}', '321dsfg1dgf22dfge568' )
print(m)


# /////////////////////////////////////////////////////
# ********************  VALIDACION ********************
# /////////////////////////////////////////////////////


# Saber si una cadena comienza con una subcadena determinada
# startswith("subcadena" [, posicion_inicio, posicion_fin])
# Retorna True o False

cadena = "bienvenido a mi aplicación".capitalize()

print('startswith\n')
print(cadena.startswith("Bienvenido"))
print(cadena.startswith("aplicación"))
print(cadena.startswith("aplicación", 16), '\n')

# Saber si una cadena finaliza con una subcadena determinada
# endswith("subcadena" [, posicion_inicio, posicion_fin])
# Retorna True o False

cadena = "bienvenido a mi aplicacion".capitalize()

print('endswith\n')
print(cadena.endswith("aplicación"))
print(cadena.endswith("Bienvenido"))
print(cadena.endswith("Bienvenido", 0, 10), '\n')

# Saber si una cadena es alfanumerica
# isalnum()
# Retorna True o False

print('isalnum\n')
cadena = "pepegrillo 75"  # contiene un espacio
print(cadena.isalnum())
cadena = "pepegrillo"
print(cadena.isalnum())
cadena = "pepegrillo75"
print(cadena.isalnum(), '\n')

# Saber si una cadena contiene unicamente digitos
# isdigit()
# Retorna True o False

print('isdigit\n')
cadena = "pepegrillo 75"
print(cadena.isdigit())
cadena = "7584"
print(cadena.isdigit())
cadena = "75 84"
print(cadena.isdigit())
cadena = "75.84"
print(cadena.isdigit(), '\n')

# Saber si una cadena contiene solo minusculas
#  islower()
# Retorna True o False

print('islower\n')
cadena = "pepe grillo"
print(cadena.islower())
cadena = "Pepe Grillo"
print(cadena.islower())
cadena = "Pepegrillo"
print(cadena.islower())
cadena = "pepegrillo75"
print(cadena.islower(), '\n')

"""
 Saber si una cadena contiene solo mayusculas
 isupper()

 Saber si una cadena contiene solo espacios en blanco
 isspace()

 Saber si una cadena tiene Formato De Titulo
 istitle()

"""


# //////////////////////////////////////////////////////
# ********************  SUSTITUCION ********************
# //////////////////////////////////////////////////////


# Dar formato a una cadena, sustituyendo texto dinamicamente
# format(*args, **kwargs)
# Retorna la cadena formateada.

cadena = "bienvenido a mi aplicación {0}"
print(cadena.format("en Python"), '\n')

cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print(cadena.format(100, 21, 121))

cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print(cadena.format(bruto=100, iva=21, neto=121))
print(cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100))

# Reemplazar texto en una cadena
# replace("subcadena a buscar", "subcadena por la cual reemplazar")
# Retorna: la cadena reemplazada.

buscar = "nombre apellido"
reemplazar = "Juan Perez"
print("Estimado Sr. nombre apellido:".replace(buscar, reemplazar), '\n')

# Eliminar caracteres a la izquierda y derecha de una cadena
# strip(["caracter"])
# Retorna la cadena sustituida.

cadena = "   www.eugeniabahit.com   "
print(cadena.strip())
print(cadena.strip(' '), '\n')


# Eliminar caracteres a la izquierda de una cadena
lstrip(["caracter"])

# Eliminar caracteres a la derecha de una cadena
rstrip(["caracter"])

# sustituir todos los numeros por guiones
m = re.sub(r'\d', '-', '345abcdser789')

# sustituir solo 4 de los numeros
m = re.sub(r'\d', '-', '345abcdser789', 4)


# /////////////////////////////////////////////////////
# *****************  UNION Y DIVISION *****************
# /////////////////////////////////////////////////////


# Unir una cadena de forma iterativa
# join(iterable)
# Retorna cadena unida con el iterable

factura = ("Nº 0000-0", "-0000 (ID: ", ")")
numero = "275"
numero_factura = numero.join(factura)
print(numero_factura, '\n')

# Partir una cadena en tres partes, utilizando un separador
# partition("separador")

# Retorna tupla de tres elementos donde el primero es el contenido de la
# cadena previo al separador, el segundo, el separador mismo y el tercero,
# el contenido de la cadena posterior al separador.

tupla = "http://www.eugeniabahit.com".partition("www.")
print(tupla, '\n')

protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}\n".format(protocolo, dominio))

# Partir una cadena en varias partes, utilizando un separador
# split("separador")
# Retorna lista con elementos encontrados al dividir cadena por separador.

keywords = "python, guia, curso, tutorial".split(", ")
print(keywords)

# Partir una cadena en lineas
# splitlines()
# Retorna lista donde cada elemento es una linea de la cadena

texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""

print(texto.splitlines())
texto = "Linea 1\nLinea 2\nLinea 3"
print(texto.splitlines())

"""
  PATRONES BASICOS

 .       cualquier caracter, excepto linea nueva
 \n      nueva linea
 \r      retorno del carro
 \t      tabulador horizontal
 \w      cualquier numero o letra minuscula
 \W      numero o letra mayuscula
 \s      espacio en blanco, tab, nueva line, retorno del carro
 \S      cualquier caracter que no es espacio en blanco
 \d      digito
 \D      cualquier caracter no numerico
 ^       inicio de cadena
 $       fin de cadena
 \       escape para caracteres especiales
 \b      separacion entre numero o letra
 +       una o mas veces
 *       cero o mas veces
 ?       cero o una vez
 {n}     el caracter se repite n veces
 []      rango, cualquier caracter entre los corchetes
 ^[]     cualquier caracter que no este en los corchetes

	PATRONES PARA COMPROBACIONES COTIDIANAS

	Numeros del 0 al 999999

	^d{1,6}$

	Codigo hexagecimal para HTML

	^#([a-fA-F0-9]){3}(([a-fA-F0-9]){3})?$

	Fecha en formato dd/mm/aaaa

	^\d\d/\d\d/\d\d\d\d$

	UNIX path

	^.*\//

	Direccion MAC

	^([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}$

	Cuenta de e-mail

	^[0-9a-zA-Z([-.\w]*[0-9a-zA-Z_+])*@([0-9a-zA-Z][-\w]*
	[0-9a-zA-Z]\.)+[a-zA-Z{2,9}]]$

	HHTP URL

	(http?):\/\/([0-9a-zA-Z][-\w+]*[0.9a-zA-Z]\.)+
	([a-zA-Z]{2,9})(:\d{1,4})?([-\w/\#~:?+=&%@~]*)

	Direccion IPv4

	^(\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(\d|[01]?\d\d|2[0-4]\d|25[0-5])\.
	(\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(\d|[01]?\d\d|2[0-4]\d|25[0-5])$

"""