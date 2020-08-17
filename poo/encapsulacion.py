class Congreso:
    def __init__(self, id, pais):
        self._id = id
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida.')

if __name__ == "__main__":
    congreso = Congreso(123, ['Medellin', 'Santa Marta'])
    # congreso.region = 'Bogota'  --> error
    print(congreso.region)