from funcionario import Funcionario


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        self.cpf = cpf
        self.nome = nome
        self.nivel = nivel
        self.diarias = 0


    def adicionar_diaria(self):
        self.diarias += 1

    def obter_diarias(self):
        return self.diarias
