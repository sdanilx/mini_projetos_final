from item import Item
from moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volume = 0
        self.volumeMaximo = volumeMaximo
        self.volume_restante = self.volumeMaximo - self.volume
        self.itens_do_cofre = ''
        self.soma_de_moedas = 0
        self.quebrou = False

    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self.volumeMaximo

    def getVolumeRestante(self):
        return self.volume_restante

    def addItem(self, item: Item):
        if self.volume == self.volumeMaximo:
            return False
        if self.quebrou == False:
            if item.volume <= self.volume_restante and item.volume <= self.volumeMaximo:
                self.volume += item.volume
                if self.itens_do_cofre:
                    self.itens_do_cofre += f", {item.descricao}"
                else:
                    self.itens_do_cofre += item.descricao
                self.volume_restante = self.volumeMaximo - self.volume
                return True
        else:
            return False

    def addMoeda(self, moeda: Moeda):
        self.moeda = moeda
        if self.volume == self.volumeMaximo:
            return False
        if self.quebrou == False:
            if 0 < moeda.value[1] <= self.volume_restante:
                self.volume += moeda.value[1]
                self.soma_de_moedas += moeda.value[0]
                self.volume_restante = self.volumeMaximo - self.volume
                return True
        else:
            return False

    def obterItens(self):
        if self.quebrou:
            if self.itens_do_cofre:
                return self.itens_do_cofre
            else:
                return 'vazio'
        else:
            return None

    def obterMoedas(self):
        if self.quebrou == True:
            return self.soma_de_moedas
        else:
            return -1

    def taInteiro(self):
        if self.quebrou == False:
            return True

    def quebrar(self):
        if not self.quebrou:
            print('Seu cofrinho está quebrado!')
            self.quebrou = True
            return True
        else:
            print('O cofrinho já está quebrado!')
            return False