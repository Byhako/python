for fila in range (10):
  for espacio in range (10 - fila):
    print(" ", end=" ")
  for columna in range (1,fila + 1):
    print(columna, end=" ")
  for columna in range (fila-1, 0, -1):
    print(columna, end=" ")
  print()
for fila in range (1, 9):
  for espacio in range (fila + 1):
    print(" ", end=" ")
  for columna in range (1, 9-fila):
    print(columna, end=" ")
  for columna in range (9-fila, 0, -1):
    print(columna, end=" ")
  print()

print()