#///////////////////////////////////////////
#***************  CREACION  ****************
#///////////////////////////////////////////

diccionario = {"color": "violeta",
               "talle": "XS",
               "precio": 174.25}

diccionario = dict(color = 'violeta',
									 taller = 'XS',
									 precio = 174)

diccionario = {clave: 1 for clave in ('x','y','z')}
diccionario = {'x':1, 'y':1, 'z':1}

diccionario.clear()  # vaciar un diccionario

# Copiar un diccionario
# copy()

diccionario = {"color": "violeta",
               "talle": "XS",
               "precio": 174.25}

remera = diccionario.copy()
musculosa = remera

"""
Si eliminamos de memoria diccionario, a remena no le pasa nada, ya que es
una copia independiente, pero si modificamos remera, se modificara tambien
musculosa, ya que se tienen dos nombres para la misma porcion de
memoria.
"""

# Crear un nuevo diccionario desde las claves de una secuencia
# dict.fromkeys(secuencia[, valor por defecto])

secuencia = ["color", "talle", "marca", 'ava']
diccionario1 = dict.fromkeys(secuencia)
diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')

# Concatenar diccionarios
# update(diccionario)

diccionario1 = {"color": "verde", "precio": 45}
diccionario2 = {"talle": "M", "marca": "Lacoste"}

diccionario1.update(diccionario2)

# //////////////////////////////////////////////////
# ******************  RETORNO  ********************
# //////////////////////////////////////////////////

# Obtener el valor de una clave
# get(clave[, "valor x defecto si la clave no existe"])

diccionario.get("color")
diccionario.get("stock", "sin stock")

# Saber si una clave existe en el diccionario

existe1 = "precio" in diccionario
# existe1 --> True

existe2 = "Sandia" in diccionario
# existe2 --> False

# Obtener las claves y valores de un diccionario
# items()

diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

for clave, valor in diccionario.items():
    print ("El valor de la clave %s es %s" %(clave, valor))
		print ("El valor de la clave {0} es {1}".format(clave, valor))


# Obtener las claves/valores de un diccionario
# keys()  values()

claves = diccionario.keys()
valores = diccionario.values()

# Eliminar elementos de diccionario

dicccionario.pop('color')  # retorna el valor -> 'rosa'
del(diccionario['color'])

# obtener una lista ordenada de las claves contenidas

lista = sorted(diccionario)

# lista con orden inverso.

lista_rev = sorted(diccionario, reverse=True)
