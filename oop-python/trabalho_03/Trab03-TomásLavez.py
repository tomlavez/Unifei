from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @abstractmethod
    def calcularSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    def calcularSalario(self):
        return self.__horasTrabalhadas * self.__valorPorHora

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
        
    @property
    def valorPorDia(self):
        return self.__valorPorDia
        
    def calcularSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia
        
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self.__valorMensal
        
    def calcularSalario(self):
        return self.__valorMensal

class MelhorOpcao(EmpDomestica):
    def __init__(self, nome, telefone, salario):
        super().__init__(nome, telefone)
        self.__salario = salario

    def calcularSalario(self):
        return self.__salario

if __name__ == "__main__":
    print()
    emp1 = Horista("Maria", 124, 160, 12)
    emp2 = Diarista("Joana", 943, 20, 65)
    emp3 = Mensalista("Tia", 9191, 1350)
    emps = [emp1, emp2, emp3]

    melhorEmp = emp1

    for op in emps:
        if op.calcularSalario() < melhorEmp.calcularSalario():
            melhorEmp = op
        print("Nome: {} - Telefone: {} - Salário Mensal: {}".format(op.nome, op.telefone, op.calcularSalario()))

    print()
    print("Melhor opção:")
    print("Nome: {} - Telefone: {} - Salário Mensal: {}".format(melhorEmp.nome, melhorEmp.telefone, melhorEmp.calcularSalario()))
    print()