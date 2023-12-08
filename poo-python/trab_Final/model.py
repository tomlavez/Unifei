from datetime import date
from copy import copy


class Produto:
    def __init__(self, codigo:str, desscricao:str, precoKg:float):
        self.__faturamento = 0
        self.__cod = codigo
        self.__descricao = desscricao
        self.precoKg = precoKg
        self.__qtdVendida = 0

    @property
    def codigo(self):
        return self.__cod

    @property
    def descricao(self):
        return self.__descricao

    @property
    def precoKg(self):
        return self.__precoKg ## '%.2f' %

    @property
    def qtdVendida(self):
        return self.__qtdVendida

    @property
    def faturamento(self):
        return self.__faturamento

    @codigo.setter
    def codigo(self, value):
        self.__cod = value

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @precoKg.setter
    def precoKg(self,newPreco:float):
        try:
            preco = float(newPreco)
            if preco < 0:
                raise ValueError
            else:
                self.__precoKg = preco
        except ValueError:
            raise ValueError('O preço deve ser um número real maior que 0')

    # a qtd vedida de produto é adicionada automaticamente ao adicionar na nota
    def _add_qtdVendida(self, qtd:float):
        self.__qtdVendida += qtd

    # a cada venda o valor é adicionado no produto
    def _add_faturamento(self, valor):
        self.__faturamento += valor


class Cliente:
    def __init__(self, nome:str, endereco:str , email:str, cpf:int):
        if not self._validar_cpf(str(cpf)):
            raise ValueError('Cpf inválido')
        else:
            self.__nome = nome
            self.__endereco = endereco
            self.__email = email
            self.__cpf = cpf
            self.__compras = []

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self) -> str:
        return str(self.__cpf)
    
    @property
    def compras(self):
        return self.__compras
    
    @compras.setter
    def compras(self, valor):
        self.__compras = valor

    # valida o cpf passado como parâmetro
    def _validar_cpf(self, cpf: str) -> bool:
        # retorna falso a quantidade de números é incompatível
        if len(cpf) != 11:
            return False

        cpfValida = cpf[0:9]
        i = 10
        soma = 0

        for num in cpfValida:
            soma += int(num) * i
            i -= 1

        soma %= 11
        soma = 11 - soma

        if soma >= 10:
            cpfValida += '0'
        else:
            cpfValida += str(soma)

        soma = 0
        i = 11

        for num in cpfValida:
            soma += int(num) * i
            i -= 1

        soma %= 11
        soma = 11 - soma

        if soma >= 10:
            cpfValida += '0'
        else:
            cpfValida += str(soma)


        # retorna true caso bater o dígito verficador e falso caso contrário
        if cpfValida == cpf:
            return True

        return False

    # todas as notas são adicionadas automaticamente ao cliente em seu contrutor
    def _add_compra(self, nota):
        self.__compras.append(nota)



class NotaFiscal:
    def __init__(self, cliente:Cliente, data:date, identificador:int):
        self.__cliente = cliente
        self.__data = data
        self.__identificador = identificador

        self.__produtos = {} # key -> produto | value -> quantidade
        self.__cliente._add_compra(self)

    ## retorna o dicionário com as quantidades vendidas
    @property
    def produtos(self):
        return self.__produtos

    @property
    def data(self) -> date:
        return self.__data

    @property
    def dataFormatada(self) -> str:
        return str(self.__data.day) + ' / '\
              + str(self.__data.month) + ' / '\
                + str(self.__data.year)

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    # adiciona produto na nota
    def add_produto(self, produto:Produto, qtd:float):
        if qtd < 0:
            raise ValueError('A quantidade de produto adicionada deve ser positiva')
        else:
            produto._add_faturamento(produto.precoKg*qtd)
            produto._add_qtdVendida(qtd)
            self.__produtos[copy(produto)] = qtd

    # retorna a quantidade de produto vedido naquela nota
    # retorna erro se não houver tal produto
    def get_qtdProduto(self, cod:str) -> float:
        for prod in self.__produtos.keys():
            if prod.codigo == cod:
                return self.__produtos[prod]

        raise ValueError('Não existe produto cadastrado com esse código')

    # calcular o valor de um certo produto de acordo com o código
    # retorna erro se não houver tal produto
    def calcular_valorProduto(self, cod:str) -> float:
        for prod in self.__produtos.keys():
            if prod.codigo == cod:
                return self.__produtos[prod] * prod.precoKg

        raise ValueError('Não existe produto cadastrado com esse código')

    # calcular o valor total da nota
    def calcular_valorNota(self) -> float:
        soma = 0
        for prod in self.__produtos.keys():
            soma += self.calcular_valorProduto(prod.codigo)

        return soma