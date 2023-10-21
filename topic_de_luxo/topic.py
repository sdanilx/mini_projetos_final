from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.vagas = capacidade
        self.vagas_normais = self.capacidade - self.qtdPrioritarios
        self.psg_normal = [None] * (capacidade - qtdPrioritarios)
        self.psg_prioritario = [None] * qtdPrioritarios
        self.lista_strings = []

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.vagas_normais

    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0 and lugar < len(self.psg_normal):
            return self.psg_normal[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if self.psg_prioritario.count(None) == 0:
            return self.psg_prioritario[lugar]
        else:
            return None

    def getVagas(self):
        return self.vagas

    def subir(self, passageiro: Passageiro):

        if self.psg_prioritario.count(None) == 0 and self.psg_normal.count(None) == 0:
            print("A topic está lotada. Não é possível inserir mais passageiros.")
            return False

        if passageiro.idade >= 65:
            if None in self.psg_prioritario:
                index = self.psg_prioritario.index(None)
                self.psg_prioritario[index] = passageiro
                self.vagas -= 1
                print(f"Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira preferencial {index}.")
                return True

            elif None in self.psg_normal:
                index = self.psg_normal.index(None)
                self.psg_normal[index] = passageiro
                self.vagas -= 1
                print(f"Não há cadeiras preferenciais disponíveis. Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira normal {index}.")
                return True

        elif passageiro.idade < 65:
            if None in self.psg_normal:
                index = self.psg_normal.index(None)
                self.psg_normal[index] = passageiro
                self.vagas -= 1
                print(f"Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira normal {index}.")
                return True
            elif None in self.psg_prioritario:
                index = self.psg_prioritario.index(None)
                self.psg_prioritario[index] = passageiro
                self.vagas -= 1
                print(f"Não há cadeiras normais disponíveis. Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira preferencial {index}.")
                return True
            return False
        return False

    def descer(self, nome: str):
        if self.psg_prioritario.count(None) == 0:
            for i, passageiro in enumerate(self.psg_prioritario):
                if passageiro and passageiro.nome == nome:
                    self.psg_prioritario.remove(passageiro)
                    self.vagas += 1
                    print(f"Passageiro {nome} desceu da cadeira preferencial.")
                    return True
            return False
        elif self.psg_normal:
            for i, passageiro in enumerate(self.psg_normal):
                if passageiro and passageiro.nome == nome:
                    self.psg_normal.remove(passageiro)
                    self.vagas += 1
                    print(f"Passageiro {nome} desceu da cadeira normal.")
                    return True
            return False
        else:
            print(f"Passageiro {nome} não encontrado na topic.")
            return False

    def toString(self):
        for passageiro in self.psg_prioritario:
            if passageiro != None:
                self.lista_strings.insert(0, '@' + passageiro.nome)
            else:
                self.lista_strings.append('@')

        for passageiro in self.psg_normal:
            if passageiro != None:
                self.lista_strings.append('=' + passageiro.nome)
            else:
                self.lista_strings.append('=')

        lista = ' '.join(self.lista_strings)
        return '[' + lista + ' ]'