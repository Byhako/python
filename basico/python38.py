# Argumentos por posición
# Expresióon por asignación
# F string con debug
# Literales -> anotaciones

from typing import Literal

# Los parametros que estan a la derecha del asterisco solo se pueden
# pasar con el nombre, no por posición.
def function1(a, b, *, c, d):
    return a + b + c + d

# Los argumentos a la izquierda solo se pueden pasar por posición
# def function2(a, b, /, c, d):
#     return a + b + c + d

def suma(a:int, b:int) -> int:
    return a + b

def uso_literales(a:int=10, users:list=[]) -> list:
    for _ in range(a):
        users.append(a)

    return users

if __name__ == "__main__":
    # F string
    nombre = 'Toto'
    saludo = f'Hola {nombre}'
    print(f'{saludo}\n')
    print(f'{saludo=}\n') # para debug


    # Literales
    print(f'11 + 13 da {suma(11, 13)}\n')
    print(f'{uso_literales(5), ["first"]}\n')
    print(f'{uso_literales(5)}\n')

    # Expresión por asignación
    """
    valor = ''
    while valor != 'quit':
        valor = input('Ingresa un valor: ')
        print('--> ', valor)
    else:
        print('Adios')
    """

    if (valor := (1 + 2)) > 2:
        print('Es mayor')

    while(valor := input('Ingresa un valor. ')) != 'quit':
        print('--> ', valor)
    else:
        print('Adios.')