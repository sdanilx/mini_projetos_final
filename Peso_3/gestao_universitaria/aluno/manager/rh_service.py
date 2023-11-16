from Peso_3.gestao_universitaria.aluno.base.funcionario import Funcionario
from Peso_3.gestao_universitaria.cliente.irh_service import IRHService
from Peso_3.gestao_universitaria.aluno.base.professor import Professor
from Peso_3.gestao_universitaria.aluno.base.sta import STA
from Peso_3.gestao_universitaria.aluno.base.terceirizado import Terceirizado


class RHService(IRHService):

    def __init__(self):
        self.funcionarios = []
        self.gratificacao = 0
        self.folha_de_pagamento = 0

        # Salário dos funcionários
        self.salario_prof_A = 3000
        self.salario_prof_B = 5000
        self.salario_prof_C = 7000
        self.salario_prof_D = 9000
        self.salario_prof_E = 11000

        # Inicado em zero pois só é calculado ao informar o nível do funcionário
        self.salario_sta = 0

        self.salario_terc = 1000
        self.salario_terc_insalubre = 1500

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
        if self.obterFuncionario(cpf):
            funcionario = self.obterFuncionario(cpf)
            if isinstance(funcionario, Professor):
                diarias = funcionario.obter_diarias()
                if diarias < 3:
                    if funcionario.classe == 'A':
                        funcionario.adicionar_diaria()
                        self.salario_prof_A += 100
                        return True
                    if funcionario.classe == 'B':
                        funcionario.adicionar_diaria()
                        self.salario_prof_B += 100
                        return True
                    if funcionario.classe == 'C':
                        funcionario.adicionar_diaria()
                        self.salario_prof_C += 100
                        return True
                    if funcionario.classe == 'D':
                        funcionario.adicionar_diaria()
                        self.salario_prof_D += 100
                        return True
                    if funcionario.classe == 'E':
                        funcionario.adicionar_diaria()
                        self.salario_prof_E += 100
                        return True
            if isinstance(funcionario, STA):
                diarias = funcionario.obter_diarias()
                if diarias < 1:
                    funcionario.adicionar_diaria()
                    self.salario_sta += 100
            if isinstance(funcionario, Terceirizado):
                return False


    def partilharLucros(self, valor: float):
        if self.funcionarios:
            self.gratificacao = valor/len(self.funcionarios)

    def iniciarMes(self):
        self.diaria_prof = 0
        self.diaria_sta = 0
        self.gratificacao = 0

    def calcularSalarioDoFuncionario(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)


        if isinstance(funcionario, Professor):
            if funcionario.classe == 'A':
                self.folha_de_pagamento += self.salario_prof_A
                return self.salario_prof_A
            if funcionario.classe == 'B':
                self.folha_de_pagamento += self.salario_prof_B
                return self.salario_prof_B
            if funcionario.classe == 'C':
                self.folha_de_pagamento += self.salario_prof_C
                return self.salario_prof_C
            if funcionario.classe == 'D':
                self.folha_de_pagamento += self.salario_prof_D
                return self.salario_prof_D
            if funcionario.classe == 'E':
                self.folha_de_pagamento += self.salario_prof_E
                return self.salario_prof_E

        elif isinstance(funcionario, STA):
            self.salario_sta += 1000 * (100 * funcionario.nivel)
            return self.salario_sta

        elif isinstance(funcionario, Terceirizado):
            if funcionario.insalubre:
                self.folha_de_pagamento += self.salario_terc_insalubre
                return self.salario_terc_insalubre
            else:
                self.folha_de_pagamento += self.salario_terc
                return self.salario_terc


    def calcularFolhaDePagamento(self):
        return self.folha_de_pagamento
