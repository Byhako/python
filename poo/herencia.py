class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    @property
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    cuadro = Cuadrado(3)
    print(cuadro.area)