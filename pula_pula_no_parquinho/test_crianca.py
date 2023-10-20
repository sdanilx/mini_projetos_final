import unittest

from crianca import Crianca


class CriancaTest(unittest.TestCase):

    def testInicializandoCrianca(self):
        crianca = Crianca("Dora", 6)
        self.assertEqual(6, crianca.getIdade(),
                     "Ao inicializar uma crianca ela deve ter a mesma idade que foi passada na inicialização")
        self.assertEqual("Dora", crianca.getName(),
                     "Ao inicializar uma crianca ela deve ter o mesmo nome que foi passada na inicialização")

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()