class Funcionario:

    def __init__(self, cpf, nome, cargo):
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self, funcionario) -> float:
        return 0.0
