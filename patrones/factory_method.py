class Cardio:
    pass


class Fuerza:
    pass


class EjercicioFactory:

    @staticmethod
    def crear(tipo):

        if tipo.lower() == "cardio":
            return Cardio()

        elif tipo.lower() == "fuerza":
            return Fuerza()

        raise ValueError("Tipo de ejercicio no válido")