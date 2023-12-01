class Espiral:
    def __init__(self):
        self.nome_do_produto = ' - '
        self.quantidade_de_produtos = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nome_do_produto

    def setNomeDoProduto(self, nome):
        self.nome_do_produto = nome
        return self.nome_do_produto

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
        return self.preco

    def getQuantidade(self):
        return self.quantidade_de_produtos

    def setQuantidade(self, quantidade):
        self.quantidade_de_produtos = quantidade
        return self.quantidade_de_produtos