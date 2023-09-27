from dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgastePorFolha(self):
        return -1

    def getDureza(self):
        return None

    def getCalibre(self):
        return -1.0

    def getTamanho(self):
        return -1

    def setTamanho(self, tamanho:int):
        pass