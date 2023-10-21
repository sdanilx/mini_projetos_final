from crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax: int):
        self.limiteMax = limiteMax
        self.caixa = 0
        self.fila_de_espera = []
        self.criancas_pulando = []

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
        for criancas in self.criancas_pulando:
            if criancas.nome != crianca.nome:
                self.fila_de_espera.append(crianca)
                return True
            else:
                return False
        return True

    def entrar(self):
        crianca = self.fila_de_espera[0]
        self.fila_de_espera.pop(0)
        self.criancas_pulando.insert(0, crianca)
        return True

    def sair(self):
        return True

    def papaiChegou(self, nome):
        return False

    def fechar(self):
        return -1