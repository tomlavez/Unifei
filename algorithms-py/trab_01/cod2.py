# 2023005057 e 2023007893

import random, math, time

# a implementação a seguir tem como ideia principal utilizar uma tabela hash para armazenar os valores da lista.
# a tabela hash é preenchida por árvores binárias de busca
# para cada valor da lista, é verificado se o complemento dele está na tabela hash


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def put(self, value):
        # insere um valor de forma ordenada na árvore binária de busca
        # retorna 1 em sucesso, e caso o valor já exista na árvore, retorna 0
        item = BinaryTree(value)
        if self.value == value:
            return 0
        if self.value > value:
            if self.left == None:
                self.left = item
                return 1
            else:
                return self.left.put(value)
        if self.value < value:
            if self.right == None:
                self.right = item
                return 1
            else:
                return self.right.put(value)
        return 0

    def get(self, value):
        # percorre a árvore binária de busca e verifica se o valor está nela
        # se estiver, retorna 1, se não, chama a função get da subárvore correspondente
        if self.value == value:
            return 1
        if self.value > value and self.left != None:
            res = self.left.get(value)
            return res
        if self.value < value and self.right != None:
            res = self.right.get(value)
            return res
        # se o valor não estiver na árvore, retorna 0
        return 0

    def checarComplemento(self, alvo, l, contador):
        # percorre a árvore binária de busca e verifica se o complemento de cada valor está na tabela
        # se estiver, incrementa o contador
        res = 0
        complemento = alvo - self.value
        res = l.get(complemento)
        if res == 1:
            contador = contador + 1
        if self.left != None:
            contador = self.left.checarComplemento(alvo, l, contador)
        if self.right != None:
            contador = self.right.checarComplemento(alvo, l, contador)
        return contador


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None for i in range(size)]

    def _hash(self, valor):
        # o valor do hash é o resto da divisão do valor pela quantidade de posições da tabela
        hashValue = 0
        hashValue = valor % self.size
        return hashValue

    def put(self, value):
        # insere um valor na tabela hash, se uma árvore binária de busca não existir na posição
        # uma nova árvore é criada, se existir, o valor é inserido na árvore.
        # retorna 1 se o valor foi inserido com sucesso e 0 se o valor já existir na árvore
        item = BinaryTree(value)
        hashValue = self._hash(value)
        position = hashValue
        if self.slots[position] == None:
            self.slots[position] = item
            return 1
        res = self.slots[position].put(value)
        return res

    def get(self, value):
        # procura a árvore binária de busca que contém o valor desejado
        # se a árvore não existir, retorna 0, se existir, chama a função get da árvore
        hashValue = self._hash(value)
        position = hashValue
        if self.slots[position] != None:
            res = self.slots[position].get(value)
            return res
        return 0

    def complemento(self, alvo, contador):
        # para cada posição da tabela hash, chama a função checarComplemento
        # que retorna a quantidade de pares que somam o valor alvo
        for i in range(0, self.size, 1):
            if self.slots[i] != None:
                contador = self.slots[i].checarComplemento(alvo, self, contador)
        return contador


tamanho = int(input())
random.seed(tamanho)
# gera uma tabela hash com tamanho/10 posições e a preenche com números aleatórios
# a tabela hash é preenchida por árvores binárias de busca

start = time.time()

l = HashTable(int(math.floor(tamanho / 10)))
cont = 0
while cont < tamanho:
    num = random.randint(0, 2**17)
    res = l.put(num)
    if res == 1:
        cont = cont + 1

end = time.time()

# gera um número alvo ímpar
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)

start = time.time()

# procura quantos pares de números na lista somam alvo
contador = 0
contador = l.complemento(alvo, contador)

end = time.time()

# imprime a quantidade de pares
# como cada par é contado duas vezes
# o contador é dividido por 2
print(contador // 2)
