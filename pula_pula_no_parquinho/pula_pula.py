from crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax: int):
        self.limiteMax = limiteMax
        self.caixa = 0
        self.fila_de_espera = [None] * limiteMax
        self.criancas_pulando = 0

    def getFilaDeEspera(self):
        return self.fila_de_espera

    def getCriancasPulando(self):
        return self.criancas_pulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        return None

    def entrarNaFila(self, crianca: Crianca):
        return True

    def entrar(self):
        return True

    def sair(self):
        return True

    def papaiChegou(self, nome):
        return False

    def fechar(self):
        return -1