from abc import ABC, abstractmethod

class IdadeInvalida(Exception):
    pass

class TitulacaoInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CpfDuplicado(Exception):
    pass

class Pessoa(ABC):
    def __init__ (self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao():
        pass

class Professor(Pessoa):
    def __init__ (self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print("Professor: {} - Endereço: {} - Idade: {} - CPF: {} - Titulação: {}".format(self.nome, self.endereco, self.idade, self.cpf, self.titulacao.lower()))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    def printDescricao(self):
        print("Aluno: {} - Endereço: {} - Idade: {} - CPF: {} - Curso: {}".format(self.nome, self.endereco, self.idade, self.cpf, self.curso.upper()))

if __name__ == "__main__":

    listaProfessor = [
        ("João", "Av Bps", 38, 1, "Doutor"),
        ("Maria", "Av Bps", 31, 2, "doutor"),
        ("Maria", "Av Bps", 31, 2, "doutor"),
        ("Roberto", "Av Bps", 29, 3, "doutor"),
        ("Pedro", "Av Bps", 36, 4, "mestre"),
    ]

    cadastro = {}

    for nome, endereco, idade, cpf, titulacao in listaProfessor:
        try:
            for x in cadastro:
                if cpf == cadastro[x].cpf:
                    raise CpfDuplicado()
            if idade < 30:
                raise IdadeInvalida()
            if titulacao.upper() != "DOUTOR":
                raise TitulacaoInvalida()
        except CpfDuplicado:
            print("Professor(a) '%s' já foi cadastrado" % nome)
        except IdadeInvalida:
            print("Professor(a) '%s' tem idade inferior a permitida" % nome)
        except TitulacaoInvalida:
            print("Professor(a) '%s' tem titulação inválida" % nome)
        else:
            cadastro[cpf] = Professor(nome, endereco, idade, cpf, titulacao)

    listaAluno = [
        ("Fabio", "Av BPS", 18, 10, "Cco"),
        ("Gabriel", "Av BPS", 22, 14, "Sin"),
        ("Fabricio", "Av BPS", 17, 11, "CCO"),
        ("Fagner", "Av BPS", 18, 12, "CCO"),
        ("Fagner", "Av BPS", 18, 12, "CCO"),
        ("Bruno", "Av BPS", 18, 13, "ECO"),
    ]

    for nome, endereco, idade, cpf, curso in listaAluno:
        try:
            for x in cadastro:
                if cpf == cadastro[x].cpf:
                    raise CpfDuplicado()
            if idade < 18:
                raise IdadeInvalida()
            if curso.upper() != "CCO" and curso.upper() != "SIN":
                raise CursoInvalido()
            
        except CpfDuplicado:
            print("Aluno(a) '%s' já foi cadastrado" % nome)
        except IdadeInvalida:
            print("Aluno(a) '%s' tem idade inferior a permitida" % nome)
        except CursoInvalido:
            print("Aluno(a) '%s' possui curso inválido" % nome)
        else:
            cadastro[nome] = Aluno(nome, endereco, idade, cpf, curso)

    print()
    print("Usuários cadastrados: ")
    for x in cadastro:
        cadastro[x].printDescricao()
