from pula_pula import PulaPula
from crianca import Crianca


class teste:
    if __name__ == '__main__':
        pulaPula = PulaPula(5)
        pulaPula.entrarNaFila(Crianca("maria", 6))
        crianca = Crianca("ana", 7)
        pulaPula.entrarNaFila(crianca)
        print(pulaPula.getFilaDeEspera())