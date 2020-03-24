import unittest

def esMayor(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaCristal(unittest.TestCase):
    def test_mayor_edad(self):
        edad = 20
        resultado = esMayor(edad)

        self.assertEqual(resultado, True)

    def test_menor_edad(self):
        edad = 5
        resultado = esMayor(edad)

        self.assertEqual(resultado, False)


if __name__ == "__main__":
    unittest.main()
