import unittest
from patrones.decorator import *

class TestDecorator(unittest.TestCase):

    def test_decorator(self):

        ejercicio = EjercicioBase()

        decorado = ConCalorias(ejercicio)

        self.assertIn("calorías", decorado.descripcion())