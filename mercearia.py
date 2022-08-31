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

# ========== VENDAS ==========
# Instanciando um produto para poder fazer a venda
# nome, preço, categoria
# x = Produtos('morango', '4', 'Frutas')

# Instanciando uma venda
# itensVendidos, vendedor, comprador, quantidadeVendida
# y = Venda(x, 'Silvana', 'Leonardo', '3')
# DaoVenda.salvar(y)
x = DaoVenda.ler()
print(x[0].comprador)