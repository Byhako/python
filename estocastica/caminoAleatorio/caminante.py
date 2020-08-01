import random

class Caminante:
    def __init__(self, nombre):
        self.nombre = nombre

class CaminanteTradicional(Caminante):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0,1), (0,-1), (1,0), (-1,0)])
