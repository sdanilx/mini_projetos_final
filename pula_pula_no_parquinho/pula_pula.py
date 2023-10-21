from crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax: int):
        self.limiteMax = limiteMax
        self.conta = 0
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
        for crianca in self.criancas_pulando:
            if crianca.nome == nome:
                return self.conta

    def entrarNaFila(self, crianca: Crianca):
        if self.fila_de_espera:
            if self.criancas_pulando:
                for criancas in self.criancas_pulando:
                    if criancas.nome != crianca.nome:
                        self.fila_de_espera.append(crianca)
                        print(f'{crianca.nome} está na fila de espera')
                        return True
                    else:
                        return False
            else:
                self.fila_de_espera.append(crianca)
                print(f'{crianca.nome} está na fila de espera')
        else:
            self.fila_de_espera.insert(0, crianca)
            print(f'{crianca.nome} está na fila de espera')
            return True

    def entrar(self):
        if len(self.criancas_pulando) < self.limiteMax and len(self.fila_de_espera) > 0:
            crianca = self.fila_de_espera[0]
            self.fila_de_espera.pop(0)
            self.criancas_pulando.insert(0, crianca)
            self.conta += 2.50
            print(f'{crianca.nome} está no pulapula')
            return True
        else:
            print('Pulapula cheio!')
            return False


    def sair(self):
        if len(self.criancas_pulando) > 0:
            crianca = self.criancas_pulando[0]
            self.criancas_pulando.pop(0)
            self.fila_de_espera.append(crianca)
            print(f'{crianca.nome} não está mais no PulaPula')
            return True
        return False

    def papaiChegou(self, nome):
        if self.criancas_pulando:
            for crianca in self.criancas_pulando:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    self.criancas_pulando.remove(crianca)
                    return True
        elif self.fila_de_espera:
            for crianca in self.fila_de_espera:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    self.fila_de_espera.remove(crianca)
                    return True
        return False

    def fechar(self):
        if self.criancas_pulando:
            self.criancas_pulando.clear()
            self.conta = None
        if self.fila_de_espera:
            self.fila_de_espera.clear()
            self.conta = None
        return -1