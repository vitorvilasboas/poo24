def validaEmail(VITOR):
    ## ESCOPO INTERNO - LOCAL
    try:
        if email.count('@') == 1 and email.split("@")[1].count(".") >= 1: return True
        else: return False
    except: return False



### ESCOPO EXTERNO - GLOBAL
agenda = []
for i in range(1, 11):
    pessoa = {}
    nome = input(f"Informe o nome do {i}º contato: ")
    cpf = input(f"Informe o CPF do {i}º contato: ")
    while True:
        email = input(f"Informe o email do {i}º contato: ")
        if validaEmail(email): break
        else: print("Email inválido!! Tente novamente.")
    pessoa = {'nome': nome, 'cpf': cpf, 'email': email}
    agenda.append(pessoa)

# agenda = [
#     {'nome':input(f"Informe o nome do {i}"),
#      'cpf': input(f"Informe o nome do {i}"),
#      'email': input(f"Informe o nome do {i}")}
#     for i in range(1, 11)
#     ]

# def validaCPF(cpf):
#     if cpf.count("-") == 1:
#         partes = cpf.split("-")
#         if len(partes[0]) == 11 and len(partes[1]) == 2:
#             p1, p2 = partes[0], partes[1]
#             if p1.count(".") == 2:
#                 if p1.split(".")[0].isnumeric() and p1.split(".")[1].isnumeric() and p1.split(".")[2].isnumeric() and p2.isnumeric():
#                     if len(p1.split(".")[0]) == 3 and len(p1.split(".")[1]) == 3 and len(p1.split(".")[2]) == 3:
#                         return True
#                     return False
#                 return False
#             return False
#         return False
#     return False

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



