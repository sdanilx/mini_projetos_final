
class Conta:

    def __init__(self, numero, saldo):
        self.numero = numero
        self.limite = 100
        self.saldo = saldo + self.limite
        self.extrato = []

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            print('Saque concluído')
        else:
            return None
        self.extrato.append(f'- {valor}')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        self.extrato.append(f'+ {valor}')

    def transferir(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino

        if origem and destino:
            if self.saldo >= valor > 0:
                origem.sacar(valor)
                destino.depositar(valor)
                print('Transação realizada')
                self.extrato.append(f'- {valor}')
            else:
                return None
    def verExtrato(self):
        return self.extrato
