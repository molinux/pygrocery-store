from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False 
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True 
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria que pretende cadastrar já existe')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover, não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print ('Categoria removida com sucesso')
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        # Reading the file and returning a list of objects.
        x = DaoCategoria.ler()
        # Filtering the list of objects and returning a list of objects that match the condition.
        # Check if categoria you want to change exists
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            # We also need to check if the new category has already exists,
            # If it already exists it will not make the change
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))

            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('A alteração foi efetuada com sucesso')
            else:
                print('A categoria que para que deseja alterar já existe')
        else:
            print('A categoria que deseja alterar não existe')

            # Let's save this in our base/file
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nehuma categoria cadastrada')
            return 0
        for i in categorias:
            print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'Produto {nome} cadastrado com sucesso !')
            else:
                print('Produto já existe no estoque')
        else:
            print('Categoria inexistente')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))

        # Check if category exists in Estoque
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            # Check if product exits in Estoque
            if len(est) > 0:
                # Add novoNome to est variable
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                # Just change if novoNome doesn't exists
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print ('Produto cadastrado com sucesso !')
                else:
                    print ('Produto já cadastrado')
            else:
                print('O produto que deseja alterar não existe')

            # Let's put it on estoque.txt
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|"
                                + i.produto.preco + "|"
                                + i.produto.categoria + "|"
                                + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('A categoria informada não existe')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            for i in estoque:
                print('========== Produto ==========')
                print(f'Nome: {i.produto.nome}\n'
                      f'Preço: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}')
                print('-------------------------')
