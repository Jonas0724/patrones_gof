class Ejercicio:

    def __init__(self):
        self.nombre = ""
        self.tipo = ""
        self.duracion = 0


class EjercicioBuilder:

    def __init__(self):
        self.ejercicio = Ejercicio()

    def set_nombre(self, nombre):
        self.ejercicio.nombre = nombre
        return self

    def set_tipo(self, tipo):
        self.ejercicio.tipo = tipo
        return self

    def set_duracion(self, duracion):
        self.ejercicio.duracion = duracion
        return self

    def build(self):
        return self.ejercicio