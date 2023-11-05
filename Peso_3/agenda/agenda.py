from contato import Contato
from identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []
        self.fones = []

    def getContatos(self) -> list:
        return sorted(self.contatos, key=lambda contato: contato.nome)

    def getQuantidadeDeContatos(self) ->  int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:
        for contatos in self.contatos:
            if contatos.nome == nome:
                return contatos
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        if contato.getFones():
            if contato.getName() not in [c.getName() for c in self.contatos]:
                self.contatos.append(contato)
                self.fones.extend(contato.getFones())
                return True
            else:
                for contatos in self.contatos:
                    if contatos.getName() == contato.getName():
                        contatos.getFones().extend(contato.getFones())
                        self.fones = contatos.getFones()
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
        if identificador is None:
            return sum(len(contato.getFones()) for contato in self.contatos)
        else:
            return sum(
                len([fone for fone in contato.getFones() if fone.identificador == identificador])
                for contato in self.contatos)

    def getQuantidadeDeFones(self):
        return len(self.fones)

    def pesquisar(self, expressao:str) -> list:
        resultados = []
        for contato in self.contatos:
            if (expressao in contato.nome or any(expressao in fone.numero for fone in contato.getFones())
                    or any(expressao in fone.identificador.value for fone in contato.getFones())):
                resultados.append(contato)
        return sorted(resultados, key=lambda contato: contato.nome)
