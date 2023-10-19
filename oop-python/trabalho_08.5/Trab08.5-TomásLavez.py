class ServicoMedico():
    def __init__ (self, dia, mes, ano, valor):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__valor = valor

    @property
    def dia(self):
        return self.__dia
    
    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def valor(self):
        return self.__valor
    
class Consulta(ServicoMedico):
    def __init__(self, dia, mes, ano, valor, nomeMedico):
        super().__init__(dia, mes, ano, valor)
        self.__nomeMedico = nomeMedico

    @property
    def nomeMedico(self):
        return self.__nomeMedico
    
class Exame(ServicoMedico):
    def __init__(self, dia, mes, ano, valor, descricao, nomeClinica, clinicaConv):
        super().__init__(dia, mes, ano, valor)
        self.__descricao = descricao
        self.__nomeClinica = nomeClinica
        self.__clinicaConv = clinicaConv

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def nomeClinica(self):
        return self.__nomeClinica
    
    @property
    def clinicaConv(self):
        return self.__clinicaConv

class Paciente():
    def __init__ (self, nome, cpf, idade, nivelPlano):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__nivelPlano = nivelPlano

        self.__listaServicos = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def nivelPlano(self):
        return self.__nivelPlano
    
    @property
    def listaServicos(self):
        return self.__listaServicos
    
    def insereConsulta(self, dia, mes, ano, valor, nomeMedico):
        self.listaServicos.append(Consulta(dia, mes, ano, valor, nomeMedico))

    def insereExame(self, dia, mes, ano, valor, descricao, nomeClinica, clinicaConv):
        self.listaServicos.append(Exame(dia, mes, ano, valor, descricao, nomeClinica, clinicaConv))

    def obtemCustoFixo(self):
        if self.idade < 19:
            if self.nivelPlano == "bronze":
                return 220
            if self.nivelPlano == "prata":
                return 320
            if self.nivelPlano == "ouro":
                return 420
        elif self.idade < 29:
            if self.nivelPlano == "bronze":
                return 320
            if self.nivelPlano == "prata":
                return 420
            if self.nivelPlano == "ouro":
                return 520
        elif self.idade < 39:         
            if self.nivelPlano == "bronze":
                return 420
            if self.nivelPlano == "prata":
                return 520
            if self.nivelPlano == "ouro":
                return 620
        elif self.idade < 49: 
            if self.nivelPlano == "bronze":
                return 520
            if self.nivelPlano == "prata":
                return 620
            if self.nivelPlano == "ouro":
                return 720
        elif self.idade < 59: 
            if self.nivelPlano == "bronze":
                return 620
            if self.nivelPlano == "prata":
                return 720
            if self.nivelPlano == "ouro":
                return 820
        else:   
            if self.nivelPlano == "bronze":
                return 720
            if self.nivelPlano == "prata":
                return 820
            if self.nivelPlano == "ouro":
                return 920            

    def calculaValorMensal(self, mes, ano):
        preco = 0
        if self.nivelPlano == "ouro":
            return self.obtemCustoFixo()
        if self.nivelPlano == "prata":
            for x in self.listaServicos:
                if mes == x.mes and ano == x.ano:
                    if type(x) is Exame:
                        if x.clinicaConv == True:
                            preco += 0.8 * x.valor
                        else:
                            preco += x.valor
                
            return (preco/2 + self.obtemCustoFixo())
        if self.nivelPlano == "bronze":
            for x in self.listaServicos:
                if mes == x.mes and ano== x.ano:
                    if type(x) is Exame:
                        if x.clinicaConv == True:
                            preco += 0.8 * x.valor
                        else:
                            preco += x.valor
                    if type(x) is Consulta:
                        preco += x.valor
            return (preco/2 + self.obtemCustoFixo())


    def imprimeServicosMes(self, mes, ano):
        print("Paciente: {}".format(self.nome))
        for x in self.listaServicos:
            if x.mes == mes and x.ano == ano:
                if type(x) is Consulta:
                    print("{}/{}/{} - Consulta: {}".format(x.dia, mes, ano, x.nomeMedico))
                elif type(x) is Exame:
                    print("{}/{}/{} - Exame: {} - Clinica {}".format(x.dia, mes, ano, x.descricao, x.nomeClinica))
        print("Valor a pagar: {:.1f}".format(self.calculaValorMensal(mes, ano)))
        print()

if __name__ == "__main__":
    listaPac = []     
    pac1 = Paciente('João Santos', '111222', 43, 'ouro')     
    pac1.insereConsulta(10, 4, 2023, 300, 'Dr. Antonio Souza')     
    pac2 = Paciente('Felipe Mendes', '222333', 35, 'prata')     
    pac2.insereConsulta(14, 4, 2023, 350, 'Dra. Ana Silva')     
    pac2.insereExame(18, 4, 2023, 500, 'Ultrasom abdomen', 'Sul Mineira', True)     
    pac3 = Paciente('Márcio Cruz', '333444', 58, 'bronze')     
    pac3.insereConsulta(7, 4, 2023, 350, 'Dra. Ana Silva')     
    pac3.insereConsulta(12, 3, 2023, 320, 'Dr. Marcelo Silveira')     
    pac3.insereConsulta(11, 4, 2023, 300, 'Dr. Antonio Souza')     
    pac3.insereExame(22, 4, 2023, 280, 'Raio X Torax', 'Radiologia Ita', False)     
    pac3.insereExame(24, 4, 2023, 250, 'Hemograma Completo', 'LabClin', True)     
    listaPac.append(pac1)     
    listaPac.append(pac2)     
    listaPac.append(pac3)     
    for pac in listaPac:         
        pac.imprimeServicosMes(4, 2023)
