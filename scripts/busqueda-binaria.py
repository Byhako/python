# -*- coding: utf-8 -*-

def search(numbers, numbersFind,  low, high):
  if (low>high):
    return False

  mitad = (low + high)//2

  if (numbers[mitad]==numbersFind):
    return True
  elif(numbers[mitad]>numbersFind):
    return search(numbers, numbersFind, low, mitad-1)
  else:
    return search(numbers, numbersFind, mitad+1, high)

# la lista debe estar ordenada
numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]

numbersFind = int(input('Ingresa un numero: '))

resultado = search(numbers, numbersFind, 0, len(numbers)-1)

if (resultado==True):
  print('Si esta en la lista.\n')
else:
  print('No esta en la lista.\n')