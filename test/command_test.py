import unittest
from patrones.command import CrearEjercicioCommand

class TestCommand(unittest.TestCase):

    def test_command(self):

        comando = CrearEjercicioCommand()

        self.assertEqual(comando.ejecutar(), "Ejecutado")