import unittest
from patrones.facade import SistemaEjerciciosFacade


class TestFacade(unittest.TestCase):

    def test_crear(self):

        facade = SistemaEjerciciosFacade()

        self.assertEqual(facade.crear(), "Creado")


if __name__ == "__main__":
    unittest.main()