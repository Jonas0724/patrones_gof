import unittest
from patrones.singleton import Conexion

class TestSingleton(unittest.TestCase):

    def test_instancia_unica(self):

        c1 = Conexion()
        c2 = Conexion()

        self.assertEqual(c1, c2)

if __name__ == "__main__":
    unittest.main()