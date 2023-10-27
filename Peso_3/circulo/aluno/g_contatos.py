from Peso_3.circulo.cliente.circulo_base import CirculoBase
from Peso_3.circulo.cliente.contato_base import ContatoBase
from Peso_3.circulo.cliente.icirculo_operations_manager import ICirculoOperationsManager
from Peso_3.circulo.cliente.icirculos_manager import ICirculosManager
from Peso_3.circulo.cliente.icontatos_manager import IContatosManager



class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):

    def createContact(self, id: str, email: str) -> bool:
        return False

    def getAllContacts(self) -> list:
        return None

    def updateContact(self, contato: ContatoBase) -> bool:
        return False

    def removeContact(self, id: str) -> bool:
        return False

    def getContact(self, id: str) -> ContatoBase:
        return None

    def getNumberOfContacts(self) -> int:
        return 0

    def favoriteContact(self, idContato: str) -> bool:
        return False

    def unfavoriteContact(self, idContato: str) -> bool:
        return False

    def isFavorited(self, id: str) -> bool:
        return False

    def getFavorited(self) -> list:
        return None

    def createCircle(self, id: str, limite: int) -> bool:
        return False

    def updateCircle(self, circulo: CirculoBase) -> bool:
        return False

    def getCircle(self, idCirculo: str) -> CirculoBase:
        return None

    def getAllCircles(self) -> list:
        return None

    def removeCircle(self, idCirculo: str) -> bool:
        return False

    def getNumberOfCircles(self) -> int:
        return 0

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