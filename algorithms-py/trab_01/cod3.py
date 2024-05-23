# 2023005057 e 2023007893

import random

# essa implementação utiliza uma árvore binária de busca para armazenar e buscar números de forma eficiente,
# e a partir disso, utiliza um conjunto para rastrear números já vistos e encontrar quantos pares na lista
# somam um valor alvo.


class TreeNode:
    def __init__(self, data):
        # Inicializa um nó da árvore binária de busca com o dado fornecida
        self.data = data
        self.left = None
        self.right = None


class BinarygetTree:
    def __init__(self):
        # Inicializa uma árvore binária de busca vazia
        self.root = None

    def put(self, data):
        # Insere um novo dado na árvore binária de busca
        # Se a raiz estiver vazia, cria um novo nó raiz
        # Caso contrário, insere recursivamente no local apropriado
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.put_recursive(self.root, data)

    def put_recursive(self, node, data):
        # Função auxiliar para inserção recursiva
        # Se o dado for menor que o dado do nó atual, vai para a subárvore esquerda
        # Se o dado for maior que o dado do nó atual, vai para a subárvore direita
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.put_recursive(node.left, data)
        elif data > node.data:  # Evita duplicatas
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.put_recursive(node.right, data)

    def get(self, data):
        # Pesquisa um dado na árvore binária de busca
        return self.get_recursive(self.root, data)

    def get_recursive(self, node, data):
        # Função auxiliar para busca recursiva
        # Se o nó atual for nulo ou o dado do nó for igual o dado procurada, retorna o nó
        # Se o dado procurada for menor que o dado do nó atual, busca na subárvore esquerda
        # Se o dado procurada for maior que o dado do nó atual, busca na subárvore direita
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.get_recursive(node.left, data)
        else:
            return self.get_recursive(node.right, data)


def count_pairs_with_sum(bst, S, k):
    # Conta quantos pares na lista S somam k usando a árvore binária de busca
    # Verifica se o complemento existe na árvore e não foi visto antes
    count = 0
    seen = set()  # Conjunto para rastrear números já vistos

    for num in S:
        complement = k - num
        if complement != num and complement not in seen and bst.get(complement):
            count += 1
            seen.add(num)
            seen.add(complement)

    return count


tamanho = int(input())  # Lê o tamanho da lista
random.seed(tamanho)

bst = BinarygetTree()
S = []

while len(S) < tamanho:
    num = random.randint(0, 2**17)
    if not bst.get(num):  # Evita duplicatas
        bst.put(num)
        S.append(num)

# Gera um número alvo ímpar
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)

# Contando os pares que somam o alvo
resultado = count_pairs_with_sum(bst, S, alvo)
print(resultado)
