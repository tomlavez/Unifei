from abc import ABC, abstractmethod
from datetime import date

class Transacao():
    def __init__ (self, data, valor, desc):
        self.__data = data
        self.__valor = valor
        self.__desc = desc
    
    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def desc(self):
        return self.__desc
    
    def printDescricao(self):
        print("     Data: {} - Valor: {} - Descrição: {}".format(self.data, self.valor, self.desc))

class Conta(ABC):
    def __init__ (self, numero, nomeCorrentista, saldo):
        self.__numero = numero
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

        self.__transacao = []

    @property
    def numero(self):
        return self.__numero
    
    @property
    def nomeCorrentista(self):
        return self.__nomeCorrentista
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def transacao(self):
        return self.__transacao
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @nomeCorrentista.setter
    def nomeCorrentista(self, nomeCorrentista):
        self.__nomeCorrentista = nomeCorrentista

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        transacao = Transacao(date.today(), +valor, "Deposito")
        self.__transacao.append(transacao)
        print("Depósito concluído!")
    
    def retirar(self, valor):
        if((self.__saldo) - (valor) >= 0):
            self.__saldo -= valor
            transacao = Transacao(date.today(), -valor, "Retirada")
            self.__transacao.append(transacao)
            print("Retirada realizada!")
        else:
            print("Saldo insuficiente!")

    @abstractmethod
    def imprimirExtrato(self):
        pass

class contaCorrenteComum(Conta):
    def __init__(self, numero, nomeCorrentista, saldo):
        super().__init__(numero, nomeCorrentista, saldo)

    def imprimirExtrato(self):
        print("Número da conta: {} - Nome do titular: {} - Saldo: {}".format(self.numero, self.nomeCorrentista, self.saldo))
        print("Transações: ")
        for tran in self.transacao:
            tran.printDescricao()
        print()
        

class contaCorrenteLimite(Conta):
    def __init__(self, numero, nomeCorrentista, saldo, limite):
        super().__init__(numero, nomeCorrentista, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def retirar(self, valor):
        if(self.saldo - valor >= -(self.limite)):
            self.saldo -= valor
            transacao = Transacao(date.today(), -valor, "Retirada")
            self.transacao.append(transacao)
            print("Retirada realizada!")
        else:
            print("Saldo insuficiente!")

    def imprimirExtrato(self):
        print("Número da conta: {} - Nome do titular: {} - Saldo: {} - Limite: {}".format(self.numero, self.nomeCorrentista, self.saldo, self.limite))
        print("Transações: ")
        for tran in self.transacao:
            tran.printDescricao()
        print()

class contaPoupanca(Conta):
    def __init__(self, numero, nomeCorrentista, saldo, diaAniv):
        super().__init__(numero, nomeCorrentista, saldo)
        self.__diaAniv = diaAniv

    @property
    def diaAniv(self):
        return self.__diaAniv
    
    @diaAniv.setter
    def diaAniv(self, diaAniv):
        self.__diaAniv = diaAniv
    
    def imprimirExtrato(self):
        print("Número da conta: {} - Nome do titular: {} - Saldo: {} - Dia do aniversário: {}".format(self.numero, self.nomeCorrentista, self.saldo, self.diaAniv))
        print("Transações: ")
        for tran in self.transacao:
            tran.printDescricao()
        print()

if __name__ == "__main__":
    conta1 = contaCorrenteComum(12, "Roberto", 122)
    conta2 = contaCorrenteLimite(13, "Joao", 145, 55)
    conta3 = contaPoupanca(15, "Alfredo", 190, 14)

    contas = [conta1, conta2, conta3]

    conta1.depositar(18)
    conta1.retirar(140)
    conta2.depositar(5)
    conta2.retirar(200)
    conta3.depositar(10)
    conta3.retirar(50)
    print()

    for c in contas:
        c.imprimirExtrato()
