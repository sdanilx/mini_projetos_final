from Peso_3.gestao_universitaria.aluno.base.funcionario import Funcionario
from Peso_3.gestao_universitaria.cliente.irh_service import IRHService
from Peso_3.gestao_universitaria.aluno.base.professor import Professor
from Peso_3.gestao_universitaria.aluno.base.sta import STA
from Peso_3.gestao_universitaria.aluno.base.terceirizado import Terceirizado


class RHService(IRHService):

    def __init__(self):
        self.funcionarios = []

    def cadastrar(self, funcionario: Funcionario):
        if isinstance(funcionario, Professor):
            if 'A' <= funcionario.classe <= 'E':
                if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
        elif isinstance(funcionario, STA):
            if 1 <= funcionario.nivel <= 30:
                if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
        else:
            if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                self.funcionarios.append(funcionario)
                return True
        return False

    def remover(self, cpf: str):
        for cadastro in self.funcionarios:
            if cadastro.cpf == cpf:
                self.funcionarios.remove(cadastro)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        for cadastro in self.funcionarios:
            if cadastro.cpf == cpf:
                return cadastro
        return None

    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda funcionario: funcionario.nome)

    def getFuncionariosPorCategorias(self, tipo):
        if tipo == tipo.PROF:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if
                                    isinstance(funcionario, Professor)]
        elif tipo == tipo.STA:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if isinstance(funcionario, STA)]

        elif tipo == tipo.TERC:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if
                                    isinstance(funcionario, Terceirizado)]
        else:
            return []  # Retornar uma lista vazia se o tipo não for reconhecido

        funcionarios_do_tipo.sort(key=lambda x: x.nome)
        return funcionarios_do_tipo

    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        return False

    def partilharLucros(self, valor: float):
        return False

    def iniciarMes(self):
        pass

    def calcularSalarioDoFuncionario(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.classe == 'A':
                return 3000.0
            if funcionario.classe == 'B':
                return 5000.0
            if funcionario.classe == 'C':
                return 7000.0
            if funcionario.classe == 'D':
                return 9000.0
            if funcionario.classe == 'E':
                return 11000.0

        elif isinstance(funcionario, STA):
            nivel = funcionario.nivel
            salario_base = 1000 + 100 * nivel if 1 <= nivel <= 30 else 0
            return salario_base

        elif isinstance(funcionario, Terceirizado):
            salario_base = 1500 if funcionario.insalubre else 1000
            return salario_base




    def calcularFolhaDePagamento(self):
        return 0
