from Peso_3.circulo.aluno.base.circulo import Circulo
from Peso_3.circulo.aluno.base.contato import Contato
from Peso_3.circulo.cliente.icirculo_operations_manager import ICirculoOperationsManager
from Peso_3.circulo.cliente.icirculos_manager import ICirculosManager
from Peso_3.circulo.cliente.icontatos_manager import IContatosManager
from Peso_3.circulo.cliente.contato_not_found_exception import ContatoNotFoundException
from Peso_3.circulo.cliente.circulo_not_found_exception import CirculoNotFoundException

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
            if contato.getId() == id:
                self.contatos.remove(contato)
                for circulo in self.circulos:
                    for contato in circulo.contatos:
                        if contato.getId() == id:
                            circulo.contatos.remove(contato)
                if contato in self.contatos_favoritos:
                    self.contatos_favoritos.remove(contato)
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
            return sorted(self.contatos_favoritos, key=lambda contato: contato.getId())
        else:
            return None

    def createCircle(self, id: str, limite: int) -> bool:
        circulo = Circulo(id, limite)
        if circulo.id not in [c.id for c in self.circulos]:
            self.circulos.append(circulo)
            return True
        return False

    def updateCircle(self, circulo: Circulo) -> bool:
        for existing_circle in self.circulos:
            if existing_circle.getId() == circulo.getId():
                if circulo.getLimite() > 0:
                    existing_circle.setLimite(circulo.getLimite())
                    return True
                return False
        return None

    def getCircle(self, idCirculo: str) -> Circulo:
        for circulo in self.circulos:
            if circulo.getId() == idCirculo:
                return circulo
        return None

    def getAllCircles(self) -> list:
        return sorted(self.circulos, key= lambda circulo: circulo.getId())

    def removeCircle(self, idCirculo: str) -> bool:
        for circulo in self.circulos:
            if circulo.id == idCirculo:
                self.circulos.remove(circulo)
                return True
        return False

    def getNumberOfCircles(self) -> int:
        return len(self.circulos)

    def tie(self, idContato: str, idCirculo: str) -> bool:
        try:
            circulo = self.getCircle(idCirculo)
            if circulo is None:
                raise CirculoNotFoundException(idCirculo)

        except CirculoNotFoundException as errorNotFound:
            raise errorNotFound

        try:
            contato = self.getContact(idContato)
            if contato is None:
                raise ContatoNotFoundException(idContato)

        except ContatoNotFoundException as errorCNF:
            raise errorCNF

        if contato in circulo.contatos:
            return False

        if len(circulo.contatos) >= circulo.limite:
            return False
        else:
            circulo.contatos.append(contato)
            return True

    def untie(self, idContato: str, idCirculo: str) -> bool:
        try:
            circulo = self.getCircle(idCirculo)
            if circulo is None:
                raise CirculoNotFoundException(idCirculo)
        except CirculoNotFoundException as errorCirculoNotFound:
            raise errorCirculoNotFound

        try:
            contato = self.getContact(idContato)
            if contato is None:
                raise ContatoNotFoundException(idContato)

        except ContatoNotFoundException as errorCNF:
            raise errorCNF

        if circulo.contatos is None or contato not in circulo.contatos:
            return False
        else:
            circulo.contatos.remove(contato)
            return True

    def getContacts(self, id: str) -> list:
        try:
            circulo = self.getCircle(id)
            contatos = circulo.contatos
            if contatos is None:
                raise ContatoNotFoundException(contatos)
            contatos_ordenados = sorted(contatos, key=lambda contato: contato.id)
            return contatos_ordenados

        except CirculoNotFoundException(id) as errorCirculoNotFound:
            raise errorCirculoNotFound



    def getCircles(self, id: str) -> list:
        try:
            self.getContact(id)
            contato = self.getContact(id)
            if contato is None:
                raise ContatoNotFoundException(id)
            circulos_com_contato = [circulo for circulo in self.circulos if contato in circulo.contatos]
            circulos_ordenados = sorted(circulos_com_contato, key=lambda circulo: circulo.id)

            return circulos_ordenados

        except ContatoNotFoundException(id) as errorCNF:
            raise errorCNF



    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:

        try:
            circulos_em_comum = []
            for circulo in self.getCircles(idContato1):
                for circulo2 in self.getCircles(idContato2):
                    if circulo == circulo2:
                        circulos_em_comum.append(circulo)

            circulos_ordenados = sorted(circulos_em_comum, key=lambda circulo: circulo.id)

        except ContatoNotFoundException as errorCNF:
            raise errorCNF

        return circulos_ordenados
