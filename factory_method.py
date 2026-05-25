class Ejercicio:
    pass

class Cardio(Ejercicio):
    pass

class Fuerza(Ejercicio):
    pass

class EjercicioFactory:

    @staticmethod
    def crear(tipo):
        if tipo == "cardio":
            return Cardio()

        if tipo == "fuerza":
            return Fuerza()