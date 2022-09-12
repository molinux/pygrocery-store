from multiprocessing.connection import Client
from Controller import ControllerCategoria
from DAO import *

# Let's test this !

# ========== CATEGORIAS ==========
# Salvar
# DaoCategoria.salvar('Frutas')
# DaoCategoria.salvar('Verduras')
# DaoCategoria.salvar('Legumes')
# Ler
# for i in DaoCategoria.ler():
#     print(i.categoria)
a = ControllerCategoria()
# a.cadastrarCategoria('Frios')
a.removerCategoria('Legumes')

# ========== VENDAS ==========
# Instanciando um produto para poder fazer a venda
# nome, preço, categoria
# x = Produtos('morango', '4', 'Frutas')

# Instanciando uma venda
# itensVendidos, vendedor, comprador, quantidadeVendida
# y = Venda(x, 'Silvana', 'Leonardo', '3')
# DaoVenda.salvar(y)
# x = DaoVenda.ler()
# print(x[0].comprador)

# ========== ESTOQUE ==========
# x = Produtos('Banana', '4', 'Frutas')
# DaoEstoque.salvar(x, 20)
# x = DaoEstoque.ler()
# print(f"{x[0].produto.nome}, {x[0].quantidade}")

# ========== FORNECEDORES ==========
# x = Fornecedor('Arita Comércio', '98787654323456', '2299887766', 'Verduras')
# DaoFornecedor.salvar(x)
# x = DaoFornecedor.ler()
# print(x[0].nome, x[0].cnpj)

# ========== CLIENTES ==========
# x = Pessoa('Andressa Santos', '99877788', '98789876545', 'andressa.santos@uol.com.br', 'Rua Olavo Bilac, 456 - Tijuca')
# DaoPessoa.salvar(x)
# x = DaoPessoa.ler()
# print(x[0].nome, x[0].email)

# ========== FUNCIONARIOS ==========
# x = Funcionario('99999999999999', 'Luisa Andressa', '2198778899', '96877897877', 'luisa.andressa@gmail.com', 'Rua dos Abrólios, 444')
# DaoFuncionario.salvar(x)
# x = DaoFuncionario.ler()
# print(x[0].clt, x[0].nome)