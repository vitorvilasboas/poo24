
## Criar classe PRODUTO
class Produto:
    def __init__(self):  ## método construtor
        self.marca = None
        self.modelo = None
        self.tipo = None
        self.preco = None
        self.cliente = None


# Instanciar o objeto da classe PRODUTO
prod1 = Produto()
prod1.marca = "FIAT"
prod1.modelo = "ARGO"
prod1.preco = 95900

prod2 = Produto() ## instanciando outro produto da classe 2

print(prod1.marca, prod2.marca)



