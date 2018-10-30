n = int(input('Ingresa un número natural: '))
print('\nLos fatores primos para los números ente 2 y',n,'son:\n')

primos = [2]

def addPrimo():
  """
  agrego le siguiente primo a la lista primos
  """
  numero = primos[-1] # last primo

  while True:
    numero += 1
    for primo in primos:
      if not numero%primo:
        break
    if not numero % primo:
      continue
    else: 
      primos.append(numero)
      break


for i in range(2,n+1):
  numero = i
  lista = []
  while True:
    for primo in primos:
      while numero%primo==0:
        lista.append(primo)
        numero = numero/primo
      if numero==1: break
    if numero==1:
      print(i,'-->',lista)
      break
    else:
      addPrimo()

"""
Verifico que el numero pueda ser dividido entre primo(29), si es asi, agrego ese
primo a la lista(30), y continuo con el resultado de la division. 
Si numero/primo = 0 entonces ya termine y salgo(32,34), si no, entonces agrego
el siguiente primo a la lista y repito el proceso.
"""