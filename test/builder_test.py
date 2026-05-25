import unittest
from patrones.builder import EjercicioBuilder

class TestBuilder(unittest.TestCase):

    def test_builder(self):

        ejercicio = (
            EjercicioBuilder()
            .set_nombre("Sentadillas")
            .set_tipo("Fuerza")
            .set_duracion(30)
            .build()
        )

        self.assertEqual(ejercicio.nombre, "Sentadillas")
        self.assertEqual(ejercicio.tipo, "Fuerza")
        self.assertEqual(ejercicio.duracion, 30)