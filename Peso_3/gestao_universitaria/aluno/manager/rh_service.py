from Peso_3.gestao_universitaria.aluno.base.funcionario import Funcionario
from Peso_3.gestao_universitaria.cliente.irh_service import IRHService
from Peso_3.gestao_universitaria.aluno.base.professor import Professor
from Peso_3.gestao_universitaria.aluno.base.sta import STA
from Peso_3.gestao_universitaria.aluno.base.terceirizado import Terceirizado
from Peso_3.gestao_universitaria.cliente.tipo import Tipo


class RHService(IRHService):

    def __init__(self):
        self.funcionarios = []
        self.gratificacao = 0

        # Salário dos professores e terceirizados
        self.salarios = {
            'A': 3000,
            'B': 5000,
            'C': 7000,
            'D': 9000,
            'E': 11000, 'terc_ins': 1500, 'terc': 1000}

        # Salário do STA inicado em zero pois só é calculado ao informar o nível do funcionário
        self.salario_sta = 0


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
                return False
            return False

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
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.obter_diarias() < 3:
                funcionario.adicionar_diaria()
                return True
            return False
        elif isinstance(funcionario, STA):
            if funcionario.obter_diarias() < 1:
                funcionario.adicionar_diaria()
                return True
            return False
        elif isinstance(funcionario, Terceirizado):
            return False



    def partilharLucros(self, valor: float):
        if self.funcionarios:
            self.gratificacao = valor/len(self.funcionarios)
            return True

    def iniciarMes(self):
        self.salarios = {
            'A': 3000,
            'B': 5000,
            'C': 7000,
            'D': 9000,
            'E': 11000, 'terc_ins': 1500, 'terc': 1000}
        self.salario_sta = 0
        self.gratificacao = 0
        return True

    def calcularSalarioDoFuncionario(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.obter_diarias() > 0:
                salario = self.salarios[funcionario.classe] + (funcionario.obter_diarias() * 100) + self.gratificacao

                return salario
            else:
                return self.salarios[funcionario.classe] + self.gratificacao

        elif isinstance(funcionario, STA):
            if funcionario.obter_diarias() == 1:
                self.salario_sta = 1000 + (100 * funcionario.nivel) + 100 + self.gratificacao
                return self.salario_sta
            else:
                self.salario_sta = 1000 + (100 * funcionario.nivel) + self.gratificacao
                return self.salario_sta

        elif isinstance(funcionario, Terceirizado):
            if funcionario.insalubre:
                return self.salarios['terc_ins'] + self.gratificacao
            else:
                return self.salarios['terc'] + self.gratificacao


    def calcularFolhaDePagamento(self):
        self.folha_de_pagamento = 0

        if self.funcionarios:
            professores = self.getFuncionariosPorCategorias(Tipo.PROF)
            stas = self.getFuncionariosPorCategorias(Tipo.STA)
            tercs = self.getFuncionariosPorCategorias(Tipo.TERC)

            for professor in professores:
                salario = self.calcularSalarioDoFuncionario(professor.cpf)
                self.folha_de_pagamento += salario

            for sta in stas:
                salario = self.calcularSalarioDoFuncionario(sta.cpf)
                self.folha_de_pagamento += salario

            for terc in tercs:
                salario = self.calcularSalarioDoFuncionario(terc.cpf)
                self.folha_de_pagamento += salario

            self.folha_de_pagamento

            return self.folha_de_pagamento
        return 0
