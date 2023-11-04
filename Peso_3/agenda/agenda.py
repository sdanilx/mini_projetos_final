from contato import Contato
from identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []
        self.fones = []

    def getContatos(self) -> list:
        return self.contatos

    def getQuantidadeDeContatos(self) ->  int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:
        for contatos in self.contatos:
            if contatos.nome == nome:
                return self.contatos
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        if contato.getName() not in [c.getName() for c in self.contatos]:
            self.contatos.append(contato)
            self.fones.extend(contato.getFones())
            return True
        else:
            for contatos in self.contatos:
                if contatos.getName() == contato.getName():
                    contatos.getFones().extend(contato.getFones())
                    self.fones.extend(contatos.getFones)
                    return False
        return False

    def removerContato(self, nome: str) -> bool:
        for contatos in self.contatos:
            if contatos.nome == nome:
                self.contatos.remove(contatos)
                return True

    def removerFone(self, nome:str, index: int) -> bool:
        if index <= len(self.fones):
            for contato in self.contatos:
                if contato.getName() == nome:
                    contato.getFones().pop(index)
                    self.fones.pop(index)
                    return True
        return False

    def getQuantidadeDeFones(self, identificador: Identificador) -> int:
        pass
    def getQuantidadeDeFones(self) -> int:
        pass
    def pesquisar(self, expressao:str) -> list:
        return None
