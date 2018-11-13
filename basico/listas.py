# -*- coding: utf-8 -*-
# /////////////////////////////////////////////////////
# ********************  AGREGADO  ********************
# /////////////////////////////////////////////////////

# Agregar un elemento al final de la lista
# append("nuevo elemento")

nombres = ["Alvaro", "Jacinto", "Miguel", "Edgardo"]
nombres.append("Jose")

# Agregar varios elementos al final de la lista
# extend(otra_lista)

nombres.extend(["Jose", "Gerardo"])

# Agregar un elemento en una posicion determinada
# insert(posición, "nuevo elemento")

nombres.insert(0, "Ricky")

# Creacion por comprension.

lista = [i for i in range(20)]

# ///////////////////////////////////////////////////////
# ********************  ELIMINACION  ********************
# ///////////////////////////////////////////////////////

# Eliminar el ultimo elemento de la lista
# pop()

nombres.pop()

# Eliminar un elemento por su indice
# pop(índice)

nombres.pop(3)

# Eliminar un elemento por su valor
# remove("valor")

nombres.remove("Jose")

# //////////////////////////////////////////////////
# ********************  ORDEN  ********************
# //////////////////////////////////////////////////

# Invertir orden
# reverse()

nombres.reverse()

# Orden ascendente
# sort()

nombres.sort()

# Orden descendente
# sort(reverse=True)

nombres.sort(reverse=True)

# /////////////////////////////////////////////////////
# ********************  BUSQUEDA  ********************
# /////////////////////////////////////////////////////

# Contar cantidad de apariciones elementos
# count(elemento)

nombres.count("Miguel")

# Obtener numero de indice
# index(elemento[, indice_inicio, indice_fin])

nombres.index("Miguel")
nombres.index("Miguel", 2, 5)

# ///////////////////////////////////////////////////
# ********************  EXTRAS  ********************
# ///////////////////////////////////////////////////

tupla = (1, 2, 3, 4)
list(tupla)

lista = [1, 2, 3, 4]
tuple(lista)

conjunto = {1,2,2,3}  # conserva elementos sin repetir
con = set(lista)

max(tupla)
min(lista)
