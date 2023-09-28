from dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgastePorFolha(self):
        return self.dureza

    def getDureza(self):
        return self.dureza

    def getCalibre(self):
        return self.calibre

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho:int):
        self.tamanho = tamanho