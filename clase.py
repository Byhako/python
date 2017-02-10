from math import pi

#==========================================================

class Moto:
  nRuedas = '2'  # variable de clase

  def __init__(self, marca, modelo, color):
    self.marca = marca     # variable de instancia
    self.modelo = modelo
    self.color =  color
    print('Constructor ejecutado')

  def get_marca(self):     #  Metodo de instancia
    print(self.marca)

  def __del__(self):
    print('del')

#==========================================================

class Circulo:
  def __init__(self,radio):
    self.radio = radio

  @property    # Decorador o modificador
  def area(self):
    return pi * (self.radio**2)

  def areas(self):
    return pi * (self.radio**2)

# en lugar de usar el decorador, se puede definir el metodo en la clase
# y luego usar la funcion property() para convertirlo en un atributo

  def arrea(self):
    return pi * (self.radio**2)
  arrea = property(arrea)

  def tono(self, color):
    self.color = color

#==========================================================

class Figura:
  @property
  def radius(self):
    return self.__radio

  @radius.setter
  def radio(self, radio):
    self.__radio = radio

#==========================================================

class privado:
  def __init__(self):
    self.__atributo = 9

#==========================================================

class Test:
  def __init__(self):
    self.x = 8

  @classmethod
  def metodoClase(cls,parametro):
    print(parametro)

  @staticmethod
  def metodoEstatico(valor):
    print('Metodo estatico -> ',valor)
#==========================================================
class Ini:
  def __new__(cls,x):  # Creacion de instancia
    print('new')
    return super(Ini, cls).__new__(cls)

  def __init__(self,x):  # Inicializacion de instancia
    self.x = 9
    print('init')

#==========================================================

a = Moto('Kawasaky','Vulcan','blanco')

print('marca: ',a.marca)
print('ruedas: ',a.nRuedas)

cir = Circulo(2)
print('Area: ',cir.area )     # no se necesitan parentesis al final
print('Area: ',cir.areas() )  # si se necesitan parentesis al final
print('Area: ',cir.arrea )

bola = Figura()
bola.radio = 3
print('Radio bola: ', bola.radio)

col = 'verde'
cir.tono(col)
print(cir.color)

Test.metodoClase('Metodo de clase')
Test.metodoEstatico(33)

obj = Ini(8)

# //////////////////////////////////////////
#                HERENCIA
# //////////////////////////////////////////

class abuelo:
  def mAbuelo(self):
    print("clase abuelo")

class Padre(abuelo):
  def __init__(self):
    self.atributo = 8

  def mPadre(self):
    print("Clase padre")

class Madre:
  def mMadre(self):
    print("clase madre")

class Hija(Padre, Madre):  #  Herencia multiple
  def mHija(self):
    print("Clase hija")

h = Hija()
h.mPadre()
h.mHija()
h.mAbuelo()
h.mMadre()
"""
El doble guion bajo sirve para crear un atributo privado  seld.__radio

Con el decorador @property podemos acceder al atributo area, pero no modifi
carlo, para modificalo se necesita usar setter -> Figura

No se puede acceder a un atributo privado.  

Los metodos de clase pueden ser invocados sin crear un objeto

El metodo estatico no necesita ningun argumento como parametro, ni 
a la instancia ni a la clase, pero no puede acceder a los atributos
de la clase.

Cuando __new__() recibe parametros, estos mismos deben estar en el 
metodo __init__()

Funciones especiales de comparacion:
  __it__()  -> mmenor que
  __le__()  -> menor o igual
  __gt__()  -> mayor que
  __ge__()  -> mayor o igual
  __eq__()  -> igual que
  __ne__()  -> distinto que

  def __gt__(self,otro):
    if self.instancia > otro.instancia:
      return True
    else:
      return False

Funcion hash

objeto.__hash__()
hash(objeto)

 INTROSPECCION

dir(objeto) -> devuelve todos los metodos que pueden ser invocados
isinstance(objeto,clase) -> para comprobar si un objeto es instancia de una clase
hasattr(objeto,'atributo') -> para saber si un objeto tiene un atributo dado
callable(objeto.metodo) -> devuelve True si puede ser llamado como funcion.
objeto.__getattribute__('atributo') = objeto.atributo
objeto.__setattr('atributo','valor') ->  objeto.atributo = valor

"""