from funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        self.cpf = cpf
        self.nome = nome
        self.classe = classe
        self.diarias = 0

    def adicionar_diaria(self):
        self.diarias += 1

    def obter_diarias(self):
        return self.diarias
