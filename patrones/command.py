class Comando:

    def ejecutar(self):
        pass


class CrearEjercicioCommand(Comando):

    def ejecutar(self):
        print("Ejercicio creado")