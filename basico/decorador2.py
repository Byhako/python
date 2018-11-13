
PASSWORD = '12345'

def password_require(func):
  def wrapper():
    password = input('Contrasena: ')

    if (password == PASSWORD):
      return func()
    else:
      print('Incorrecto.')

  return wrapper

@password_require
def need_password():
  print('La contrasena es correcta.')



def upper(func):
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result.upper()

  return wrapper

@upper
def say_my_name(name):
  return 'Hola {}'.format(name)



if __name__ == '__main__':
  #need_password()
  print(say_my_name('Ruben'))