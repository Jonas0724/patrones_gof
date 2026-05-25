class EjercicioBase:

    def descripcion(self):
        return "Ejercicio básico"


class DecoradorEjercicio:

    def __init__(self, ejercicio):
        self.ejercicio = ejercicio

    def descripcion(self):
        return self.ejercicio.descripcion()


class ConCalorias(DecoradorEjercicio):

    def descripcion(self):
        return super().descripcion() + " + calorías"