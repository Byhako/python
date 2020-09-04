import time

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial_recursivo(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

if __name__ == "__main__":
    n = 90000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'Tiempo factorial {final - comienzo}')

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(f'Tiempo factorial recursivo {final - comienzo}')