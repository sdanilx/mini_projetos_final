class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax

        self.energiaAtual = energiaMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaAtual = limpezaMax
        self.idadeAtual = 0

        self.diamantes = 0
        self.vivo = True

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energiaAtual > 0 and self.saciedadeAtual > 0 and self.limpezaAtual > 0 and self.idadeAtual != self.idadeMax:
            self.vivo = True
            return True
        else:
            self.vivo = False
            return False

    def brincar(self):
        if self.getEstaVivo() == True:
            print('Você está brincando!')
            self.energiaAtual -= 2
            self.saciedadeAtual -= 1
            self.limpezaAtual -= 3
            self.diamantes += 1
            if self.energiaAtual < 0:
                self.energiaAtual = 0
            if self.saciedadeAtual < 0:
                self.saciedadeAtual = 0
            if self.limpezaAtual < 0:
                self.limpezaAtual = 0
            if self.idadeAtual + 1 <= self.idadeMax:
                self.idadeAtual += 1
                return True
            return False
        return False

    def comer(self):
        if self.getEstaVivo() == True:
            print('Você está comendo!')
            self.energiaAtual -= 1
            self.limpezaAtual -= 2
            if self.energiaAtual < 0:
                self.energiaAtual = 0
            if self.limpezaAtual < 0:
                self.limpezaAtual = 0
            if self.idadeAtual + 1 <= self.idadeMax:
                self.idadeAtual += 1
            if self.saciedadeAtual + 4 <= self.saciedadeMax:
                self.saciedadeAtual += 4
            else:
                self.saciedadeAtual = self.saciedadeMax
                return True
        return False

    def dormir(self):
        if self.getEstaVivo() == True:
            if self.energiaMax - self.energiaAtual >= 5:
                self.idadeAtual += self.energiaMax - self.energiaAtual
                if self.idadeAtual > self.idadeMax:
                    self.idadeAtual = self.idadeMax
                self.energiaAtual = self.energiaMax
                self.saciedadeAtual -= 2
                print('Você está dormindo!')
                return True
            return False
        return False

    def banhar(self):
        if self.getEstaVivo() == True:
            self.energiaAtual -= 3
            self.saciedadeAtual -= 1
            self.limpezaAtual = self.limpezaMax
            if self.idadeAtual + 2 <= self.idadeMax:
                self.idadeAtual += 2
            else:
                self.idadeAtual = self.idadeMax
            return True
        return False