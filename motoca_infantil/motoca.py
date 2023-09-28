from pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.distancia_percorrida = 0
        self.tempo = 0
        self.pessoa_contador = 0
        self.pessoa_embarcada = None

    def getPessoa(self):
        return self.pessoa_embarcada

    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa_contador == 0:
            self.pessoa_embarcada = pessoa
            self.pessoa_contador += 1
            return True
        return False

    def descer(self):
        if self.pessoa_contador == 1:
            self.pessoa_contador -= 1
            self.pessoa_embarcada = None
            return True
        return False

    def colocarTempo(self, tempo: int):
        if tempo > 0:
            self.tempo = tempo
            return True
        return False

    def dirigir(self, tempo: int):
        if self.pessoa_contador == 1 and self.pessoa_embarcada.idade <= 10 and self.tempo > 0:
            if tempo >= self.tempo:
                self.tempo = 0
                return True
            else:
                self.tempo -= tempo
                return True
        return False

    def buzinar(self):
        if self.pessoa_contador == 1:
            e = self.potencia * "e"
            return "P" + e + "m"
        return ''