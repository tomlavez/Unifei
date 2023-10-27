from datetime import date
    
class Transacao:
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data

    
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha


class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf
   
    @property
    def senha(self):
        return self.__senha

    @property
    def tipoTransf(self):
        return self.__tipoTransf


class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante
    
    @property
    def nomeDepositante(self):
        return self.__nomeDepositante

class Conta:
    def __init__(self, nroConta, nome, limite, senha): 
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha

        self.__transacoes = [] 

    @property
    def nroConta(self):
        return self.__nroConta
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def limite(self):
        return self.__limite

    @property
    def senha(self):
        return self.__senha
    
    @property
    def transacoes(self):
        return self.__transacoes

    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)
        self.__transacoes.append(deposito)

    def adicionaSaque(self, valor, data, senha):
        if senha != self.senha or valor > self.calculaSaldo(): 
            return False            
        saque = Saque(valor, data, senha)
        self.__transacoes.append(saque)
        return True

    def adicionaTransf(self, valor,data, senha, contaFavorecido):
        if senha != self.senha or valor > self.calculaSaldo(): 
            return False
        tDebito = Transferencia(valor, data, senha, "D") 
        self.__transacoes.append(tDebito)
        tCredito = Transferencia(valor, data, senha, "C") 
        contaFavorecido.transacoes.append(tCredito)
        return True
    
    def calculaSaldo(self):
        saldo = self.__limite 
        for transacao in self.__transacoes:
            if type(transacao) is Saque:
                saldo -= transacao.valor
            elif type(transacao) is Deposito:
                saldo += transacao.valor
            elif type(transacao) is Transferencia and transacao.tipoTransf == 'D':
                saldo -= transacao.valor
            elif type(transacao) is Transferencia and transacao.tipoTransf == 'C':
                saldo += transacao.valor
        return saldo

    def calculaSaldo2(self):
        saldo = self.__limite
        for trans in self.__transacoes:
            if trans.__class__.__name__ == 'Saque':
                saldo -= trans.valor            
            if trans.__class__.__name__ == 'Deposito':
                saldo += trans.valor
            if trans.__class__.__name__ == 'Transferencia':
                if trans.tipoTransf == 'D':
                    saldo -= trans.valor
                if trans.tipoTransf == 'C':
                    saldo += trans.valor

        return saldo


if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False:
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')
    
    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo()))
    print('Saldo de c2: {}'.format(c2.calculaSaldo()))
