from Peso_3.circulo.cliente.circulo_base import CirculoBase



class Circulo(CirculoBase):

    def __init__(self, id: str, limite: int):
        super().__init__(id, limite)
        self.contatos = []

    def getNumberOfContacts(self):
        return len(self.contatos)

    def setLimite(self, limite: int):
        self.limite = limite
        return self.limite

    def __eq__(self, other):
        return self.id == other.id and self.limite == other.limite
