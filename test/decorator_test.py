import unittest
from patrones.decorator import EjercicioBase, ConCalorias


class TestDecorator(unittest.TestCase):

    def test_decorator(self):

        ejercicio = EjercicioBase()

        decorado = ConCalorias(ejercicio)

        self.assertIn("calorías", decorado.descripcion())


if __name__ == "__main__":
    unittest.main()