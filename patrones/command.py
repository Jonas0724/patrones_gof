class Comando:

    def ejecutar(self):
        pass


class CrearEjercicioCommand(Comando):

    def ejecutar(self):
        return "Ejercicio creado"