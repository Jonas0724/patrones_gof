import unittest
from patrones.singleton import Conexion


class TestSingleton(unittest.TestCase):

    def test_instancia_unica(self):

        c1 = Conexion()
        c2 = Conexion()

        self.assertIs(c1, c2)

    def test_conexion(self):

        conexion = Conexion()

        self.assertEqual(
            conexion.conectar(),
            "Conectado al JSON"
        )


if __name__ == "__main__":
    unittest.main()