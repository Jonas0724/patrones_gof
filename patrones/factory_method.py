class Cardio:
    pass

class Fuerza:
    pass

class EjercicioFactory:

    @staticmethod
    def crear(tipo):
        if tipo == "cardio":
            return Cardio()

        return Fuerza()