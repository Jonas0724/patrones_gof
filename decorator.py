class EjercicioBase:

    def descripcion(self):
        return "Ejercicio básico"


class ConCalorias:

    def __init__(self, ejercicio):
        self.ejercicio = ejercicio

    def descripcion(self):
        return self.ejercicio.descripcion() + " + calorías"