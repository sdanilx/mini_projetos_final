from grafite import Grafite
from dureza import Dureza

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.grafite_contador = 0
        self.grafite_escrever = None
        self.folhas_escritas = 0
        self.gasto_do_grafite = 0

    def inserir(self, grafite: Grafite):
        if self.grafite_contador == 0 and grafite.calibre == self.calibre:
            self.grafite_contador += 1
            self.grafite_escrever = grafite
            return True
        return False

    def remover(self):
        if self.grafite_contador == 1:
            self.grafite_contador -= 1
            self.grafite_escrever = None
            self.folhas_escritas = 0
            return True
        return False

    def escrever(self, folhas: int):
        if self.grafite_contador == 1:
            self.paginas_por_grafite = self.grafite_escrever.tamanho / self.grafite_escrever.dureza
            if self.paginas_por_grafite > folhas:
                self.folhas_escritas += folhas
                self.gasto_do_grafite += folhas
                self.paginas_por_grafite -= folhas
                self.grafite_escrever.tamanho -= self.grafite_escrever.dureza * folhas
                return True
            elif folhas > self.paginas_por_grafite:
                diferenca = folhas - self.paginas_por_grafite
                self.folhas_escritas += folhas - diferenca
                self.grafite_contador = 0
                self.grafite_escrever = None
                self.paginas_por_grafite -= folhas
                print("Aviso: O grafite acabou!")
                return False
            else:
                self.grafite_contador = 0
                self.grafite_escrever = None
                self.folhas_escritas = folhas
                self.paginas_por_grafite -= folhas
                return True
        return False

    def getGrafite(self):
        if self.grafite_contador == 0:
            return None
        else:
            return self.grafite_escrever

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhas_escritas