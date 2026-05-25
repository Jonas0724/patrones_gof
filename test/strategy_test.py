import unittest
from patrones.strategy import CalculoCardio, CalculoFuerza


class TestStrategy(unittest.TestCase):

    def test_calculo_cardio(self):

        estrategia = CalculoCardio()

        resultado = estrategia.calcular(10)

        self.assertEqual(resultado, 20)

    def test_calculo_fuerza(self):

        estrategia = CalculoFuerza()

        resultado = estrategia.calcular(10)

        self.assertEqual(resultado, 50)


if __name__ == "__main__":
    unittest.main()