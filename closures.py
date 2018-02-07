def saludarFamilia(apellido):
  def nombre(nombre):
    return 'Hola {} {}'.format(nombre, apellido)
  return nombre

gomez = saludarFamilia('gomez')
torres = saludarFamilia('Torres')

print(gomez('Andrea'))
print(torres('Andrea'))