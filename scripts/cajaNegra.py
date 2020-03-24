import unittest

def suma(a, b):
    return a + b

class CajaNegra(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -2
        num_2 = -4

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -6)

if __name__ == "__main__":
    unittest.main()
