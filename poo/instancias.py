class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, oc):
        x_diff = (self.x - oc.x)**2
        y_diff = (self.y - oc.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    c1 = Coordenada(3, 7)
    c2 = Coordenada(5, 8)
    print(c1.distancia(c2))
    print(isinstance(2, Coordenada))  # para saber si 2 es instancia de Coordenada