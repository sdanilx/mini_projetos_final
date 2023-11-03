from contato import Contato
from identificador import Identificador


class Agenda:

    def getContatos(self) -> list:
        return self.contatos

    def getQuantidadeDeContatos(self) ->  int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:
        for contatos in self.contatos:
            if contatos.nome == nome:
                return self.contato
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        for contatos in self.contatos:
            if contatos != contato:
                self.contatos.append(contato)
        return True

    def removerContato(self, nome: str) -> bool:
        for contatos in self.contatos:
            if contatos.nome == nome:
                self.contatos.pop(contatos)
        return True

    def removerFone(self, nome:str, index: int) -> bool:
        return False

    def getQuantidadeDeFones(self, identificador: Identificador) -> int:
        return 0

    def getQuantidadeDeFones(self) -> int:
        return 0

    def pesquisar(self, expressao:str) -> list:
        return None
