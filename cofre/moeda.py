from enum import Enum


class Moeda(Enum):
    M10 = (0.10, 1)
    M25 = (0.25, 2)
    M50 = (0.50, 3)
    M100 = (1.00, 4)

    def __init__(self, valor: float, volume: int):
        self.valor = valor
        self.volume = volume