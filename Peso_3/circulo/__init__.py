from Peso_3.circulo.aluno.base.circulo import Circulo
from Peso_3.circulo.aluno.base.contato import Contato
from Peso_3.circulo.cliente.icirculo_operations_manager import ICirculoOperationsManager
from Peso_3.circulo.cliente.icirculos_manager import ICirculosManager
from Peso_3.circulo.cliente.icontatos_manager import IContatosManager


class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):

    def __init__(self):
        self.contatos = []
        self.contatos_favoritos = []
        self.circulos = []

    def createContact(self, id: str, email: str) -> bool:
        contato = Contato(id, email)
        if contato.id not in [c.id for c in self.contatos]:
            self.contatos.append(contato)
            return True
        return False

    def getAllContacts(self) -> list:
        return sorted(self.contatos, key=lambda contato: contato.getId())

    def updateContact(self, contato: Contato) -> bool:
        for existing_contact in self.contatos:
            if existing_contact.getId() == contato.getId():
                existing_contact.setEmail(contato.getEmail())
                return True
        return False

    def removeContact(self, id: str) -> bool:
        for contato in self.contatos:
            if contato.id == id:
                self.contatos.remove(contato)
                return True
        return False

    def getContact(self, id: str) -> Contato:
        for contato in self.contatos:
            if contato.id == id:
                return contato
        return None


    def getNumberOfContacts(self) -> int:
        return len(self.contatos)

    def favoriteContact(self, idContato: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == idContato:
                self.contatos_favoritos.append(contato)
                return True
        return False

    def unfavoriteContact(self, idContato: str) -> bool:
        for contato in self.contatos_favoritos:
            if contato.getId() == idContato:
                self.contatos_favoritos.remove(contato)
                return True
        return False

    def isFavorited(self, id: str) -> bool:
        for contato in self.contatos_favoritos:
            if contato.getId() == id:
                return True
        return False

    def getFavorited(self) -> list:
        if self.contatos_favoritos:
            return self.contatos_favoritos
        else:
            return None

    def createCircle(self, id: str, limite: int) -> bool:
        pass

    def updateCircle(self, circulo: Circulo) -> bool:
        return False

    def getCircle(self, idCirculo: str) -> Circulo:
        return None

    def getAllCircles(self) -> list:
        return self.circulos

    def removeCircle(self, idCirculo: str) -> bool:
        return False

    def getNumberOfCircles(self) -> int:
        return len(self.circulos)

    def tie(self, idContato: str, idCirculo: str) -> bool:
        return False

    def untie(self, idContato: str, idCirculo: str) -> bool:
        return False

    def getContacts(self, id: str) -> list:
        return None

    def getCircles(self, id: str) -> list:
        return None

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        return None


