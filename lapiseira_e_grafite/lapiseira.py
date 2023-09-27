from grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafite = 0

    def inserir(self, grafite: Grafite):
        if self.grafite == 0 and grafite.calibre == self.calibre:
            self.grafite += 1
            return True
        else:
            return False


    def remover(self):
        if self.grafite == 1:
            self.grafite -= 1
            return True
        return False

    def escrever(self, folhas: int):
        self.folhas = folhas
        if self.grafite == 1:
            self.folhas -= self.grafite.dureza
        return False

    def getGrafite(self):
        return None

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return -1