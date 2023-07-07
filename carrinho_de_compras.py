class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total

    def exibir_produtos(self):
        if len(self.produtos) == 0:
            print("O carrinho está vazio.")
        else:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f"- {produto.nome} (R${produto.preco:.2f})")


# Teste da classe CarrinhoDeCompras
carrinho = CarrinhoDeCompras()

# Criando alguns produtos
produto1 = Produto("Camiseta", 29.99)
produto2 = Produto("Calça", 59.99)
produto3 = Produto("Meias", 9.99)

# Adicionando os produtos ao carrinho
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)

# Exibindo os produtos presentes no carrinho
carrinho.exibir_produtos()

# Calculando o valor total da compra
valor_total = carrinho.calcular_valor_total()
print(f"Valor total da compra: R${valor_total:.2f}")
