from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
        print(f'Categoria {categoria} criada com sucesso !')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        # print (cls.categoria)

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
# DaoCategoria.ler()
# x  = DaoCategoria.ler()
# print(x[1])