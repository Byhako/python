from math import pi

#==========================================================
# BASICO

class Moto:
  nRuedas = '2'  # variable de clase

  def __init__(self, marca, modelo, color):
    self.marca = marca     # variable de instancia
    self.modelo = modelo
    self.color =  color
    print('Constructor ejecutado')

  def get_marca(self):     #  Metodo de instancia
    print(self.marca)

# --------------------------------------------------------
a = Moto('Kawasaky','Vulcan','blanco')

print('marca: ',a.marca)
print('ruedas: ',a.nRuedas,'\n')

#==========================================================
# DECORADORES

class Circulo:
  def __init__(self,radio):
    self.radio = radio

  @property   # Cambia el metodo a propiedad del objeto
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

# --------------------------------------------------------

cir = Circulo(2)
print('Area: ',cir.area )     # no se necesitan parentesis al final
print('Area: ',cir.areas() )  # si se necesitan parentesis al final
print('Area: ',cir.arrea )

col = 'verde'
cir.tono(col)
print(cir.color,'\n')

#==========================================================
# ATRIBUTO PRIVADO

class privado:
  def __init__(self):
    self.__atributo = 9

#==========================================================
# USO DE DECORADORES PARA MODIFICAR ATRIBUTO

class Figura:
  @property
  def radius(self):
    return self.__radio

  @radius.setter  #para modificar atributo radio
  def radio(self, radio):
    self.__radio = radio

# --------------------------------------------------------

bola = Figura()
bola.radio = 3
print('Radio bola: ', bola.radio,'\n')

#==========================================================
# METODOS ESPECIALES

class Ini:
  def __new__(cls,x):    # Creacion de instancia
    print('Creacion de instancia')
    return super(Ini, cls).__new__(cls)

  def __init__(self,x):  # Inicializacion de instancia
    self.x = 9
    print('Inicializacion de instancia')

  def __del__(self):
    print('Destructor','\n')

# --------------------------------------------------------

obj = Ini(8)

#==========================================================
# TIPOS DE METODOS

class Test:
  def __init__(self,var):
    self.x = var   # atributo de instancia

  # atributo propiedad
  @property
  def propiedad(self):
    print('Mi propiedad.')

  # metodo de instancia
  def metodo(self):
    print('Metodo de instancia')

  # metodo de clase
  @classmethod
  def metodoClase(cls,parametro):
    print('metodo de clase -> ',parametro)

  # metodo estatico
  # no referencia a la instancia (self), ni a la clase (cls)
  # no se puede acceder a ningun atributo de la clase
  @staticmethod
  def metodoEstatico(valor):
    print('Metodo estatico -> ',valor)

# --------------------------------------------------------

objeto = Test('atributo instancia')

print(objeto.x)          # atributo de instancia
objeto.propiedad         # atributo propiedad
objeto.metodo()          # metodo de instancia
Test.metodoClase('17')   # metodo de clase
Test.metodoEstatico(33)  # metodo estatico
print('')

#==========================================================


"""
El doble guion bajo sirve para crear un atributo privado  self.__radio

Con el decorador @property podemos acceder al atributo area, pero no modifi
carlo, para modificalo se necesita usar setter -> Figura

No se puede acceder a un atributo privado.  

Los metodos de clase pueden ser invocados sin crear un objeto

El metodo estatico no necesita ningun argumento como parametro, ni 
a la instancia ni a la clase, pero no puede acceder a los atributos
de la clase.

Cuando __new__() recibe parametros, estos mismos deben estar en el 
metodo __init__()

El destrudtor __del__() siempre se ejecuta autamticamente cuando el 
objeto ya no es necesario. Al finalizar el programa para liberar 
memoria, pero puede ser invocado para que realice mas acciones.

"""
