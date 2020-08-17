## Reescribir metodos de la clase padre

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def avanza(self):
        print('Ando pedaleando')

if __name__ == "__main__":
    persona = Persona('Toto')
    cicli = Ciclista('Lala')
    persona.avanza
    cicli.avanza