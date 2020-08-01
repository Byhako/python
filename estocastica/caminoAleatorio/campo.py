class Campo:
    def __init__(self):
        self.coordenadas_de_caminantes = {}

    def agregar_caminante(self, caminante, coordenada):
        self.coordenadas_de_caminantes[caminante] = coordenada

    def mover_caminante(self, caminante):
        delta_x, delta_y = caminante.camina()
        coordenada_actual = self.coordenadas_de_caminantes[caminante]
        coordenada_nueva = coordenada_actual.mover(delta_x, delta_y)
        self.coordenadas_de_caminantes[caminante] = coordenada_nueva

    def obtener_coordenada(self, caminante):
        return self.coordenadas_de_caminantes[caminante]