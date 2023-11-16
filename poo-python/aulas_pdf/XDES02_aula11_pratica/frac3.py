def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.num == f2.num) and (f1.den == f2.den)

class Fracao():
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den       

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        # soma a parte fracionária
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num
        novoDen = self.__den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        # numerador e denominador simplificados
        resultNum = novoNum//divComum
        resultDen = novoDen//divComum 
               
        if resultNum == resultDen:
            # resultado da soma das frações é um inteiro
            if (type(outraFrac) is FracaoMista):
                # soma resultado inteiro à parte inteira da outra fração
                return outraFrac.inteiro + resultNum / resultDen
            else:
                # o valor retornado será um inteiro, não uma fração
                return int(resultNum / resultDen)
        if resultNum < resultDen:
            # resultado da soma das frações é uma fração cujo valor é menor que 1
            if (type(outraFrac) is FracaoMista):
                return FracaoMista(outraFrac.inteiro, resultNum, resultDen)     
            else:
                return Fracao(resultNum, resultDen)
        # resultado da soma das frações é uma fração cujo valor é maior que 1
        if (type(outraFrac) is FracaoMista):
            inteiro = outraFrac.inteiro + resultNum // resultDen
        else:
            inteiro = resultNum // resultDen
        resultNum = resultNum % resultDen
        return FracaoMista(inteiro, resultNum, resultDen)
     

class FracaoMista(Fracao):
    def __init__(self, inteiro, num, den):
        super().__init__(num, den)
        self.__inteiro = inteiro 

    def __str__(self):
        return str (self.__inteiro) + " " + str(self.num) + "/" + str(self.den)     

    @property
    def inteiro(self):
        return self.__inteiro

    @inteiro.setter
    def inteiro(self, valor):
        self.__inteiro = valor

    def __add__(self,outraFrac):
        result = super().__add__(outraFrac)
        if (type(result) is FracaoMista):
            result.inteiro += self.__inteiro
            return result
        if (type(result) is Fracao):
            return FracaoMista(self.__inteiro, result.num, result.den)
        result += self.__inteiro
        return result

if __name__ == "__main__":
    frac1 = Fracao(7, 6)
    frac2 = Fracao(13, 7)
    frac3 = frac1 + frac2
    print(frac3)
    print()

    frac1 = Fracao(1, 3)
    frac2 = Fracao(2, 3)
    frac3 = frac1 + frac2
    print(frac3)
    print()

    frac1 = FracaoMista(3, 1, 2)
    frac2 = FracaoMista(4, 2, 3)
    frac3 = frac1 + frac2
    print(frac3)