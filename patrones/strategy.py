from abc import ABC, abstractmethod


class EstrategiaCalculo(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass


class CalculoCardio(EstrategiaCalculo):

    def calcular(self, valor):
        return valor * 2


class CalculoFuerza(EstrategiaCalculo):

    def calcular(self, valor):
        return valor * 5