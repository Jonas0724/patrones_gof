import unittest
from patrones.factory_method import *

class TestFactory(unittest.TestCase):

    def test_crear_cardio(self):

        ejercicio = EjercicioFactory.crear("cardio")

        self.assertIsInstance(ejercicio, Cardio)

    def test_crear_fuerza(self):

        ejercicio = EjercicioFactory.crear("fuerza")

        self.assertIsInstance(ejercicio, Fuerza)