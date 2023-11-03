from identificador import Identificador
import re

class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        padrao = r'^[0-9()-]+$'
        if re.match(padrao, numero):
            return True
        else:
            return False

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero
