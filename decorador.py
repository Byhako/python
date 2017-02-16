
# CLOSURES

def contenedora(y):
	def anidada(x):
		return x + y
	return anidada

fu1 = contenedora(2)
fu2 = contenedora(5)

print('CLOSURE\n%i   %i\n' %(fu1(5),fu2(5)))

#*****************************************************************
#             DECORADORES
#*****************************************************************
# clase como decorador

class Decorador():
	def __init__(self, f):
		self.f = f

	def __call__(self, *argumentos):
		print('inicio', self.f.__name__)
		self.f(*argumentos)
		print('fin', self.f.__name__)

@Decorador
def funcion(p1,p2,p3):
	print('Realizo mi tarea.',p1,p2,p3)

funcion(1,2,3)

print('')

#*****************************************************************
# funcion como decorador

def principal(f):
	def nueva(*argumentos):
		print('inicia', f.__name__)
		f(*argumentos)
		print('fin', f.__name__)
	return nueva

@principal
def decorada(a,b):
	print('Realizo mi tarea',a,b)

decorada('x','y')

print('')

#*****************************************************************
# decorador con parametros

def decorador_ar(ar1, ar2, ar3):
	def wrap(f):
		print('ini wrap')

		def wrapped(*arg):
			print('ini wrapped')
			print('argumentos decorador',ar1, ar2, ar3)
			f(*arg)
			print('fin wrapped')
		return wrapped
	return wrap

@decorador_ar(1,2,3)
def fun(a,b):
	print('argumentos de funcion: ',a,b)

fun('f1','f2')