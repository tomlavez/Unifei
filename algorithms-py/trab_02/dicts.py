# 2023005057 e 2023007893

import random
from collections import defaultdict


def quickselect(lista, left, right, k):
    # Enquanto a lista não estiver vazia
    while left <= right:
        # Se a lista tiver apenas um elemento, retorna esse elemento
        if left == right:
            return lista[left]

        # Escolhe um índice aleatório para o pivô
        pivot_index = random.randint(left, right)
        # Particiona a lista em relação ao pivô
        pivot_index = partition(lista, left, right, pivot_index)
        # Se o pivô é o k-ésimo menor elemento, retorna o pivô
        if pivot_index == k:
            return lista[pivot_index]
        # Se o pivô está à direita do k-ésimo menor elemento, atualiza o limite direito
        elif pivot_index > k:
            right = pivot_index - 1
        # Se o pivô está à esquerda do k-ésimo menor elemento, atualiza o limite esquerdo
        else:
            left = pivot_index + 1
    return lista[left]


def partition(lista, left, right, pivot_index):
    # Obtém o valor do pivô
    pivot_value = lista[pivot_index]
    # Move o pivô para o final da lista
    lista[pivot_index], lista[right] = lista[right], lista[pivot_index]

    # Índice de armazenamento para os elementos menores que o pivô
    meio = left

    # Para cada elemento da lista
    for i in range(left, right):
        # Se ele é menor que o pivô, move-o para a esquerda
        if lista[i] < pivot_value:
            lista[meio], lista[i] = lista[i], lista[meio]
            # Atualiza o índice
            meio += 1
    # Move o pivô para a posição correta
    lista[meio], lista[right] = lista[right], lista[meio]
    # Retorna o índice do pivô
    return meio


def dict_sort(lista):
    # Cria um dicionário com listas vazias
    dict_tamanho = defaultdict(list)
    # Adiciona os números à lista correspondente ao seu tamanho
    for num in lista:
        length = len(str(num))
        dict_tamanho[length].append(num)
    return dict_tamanho


def kSelect(dict_tamanho, k):
    # Obtém uma lista das chaves do dicionário
    lengths = list(dict_tamanho.keys())

    # Ordena a lista
    lengths.sort()

    # Procura o dicionário que contém o k-ésimo menor elemento
    for chave in lengths:
        lista_atual = dict_tamanho[chave]
        # Se o k-ésimo menor elemento está na lista atual
        if k <= len(lista_atual):
            # Retorna o k-ésimo menor elemento
            return quickselect(lista_atual, 0, len(lista_atual) - 1, k - 1)
        # Se não, move para a próxima lista, ajustando o valor de k para a próxima lista
        k -= len(lista_atual)
    # Se não encontrou o k-ésimo menor elemento, retorna None
    return None


def main():
    ## NÃO ALTERE AS 5 LINHAS CÓDIGO ABAIXO ##
    n, k = map(int, input().strip().split())
    random.seed(48 + n + k)
    A = [random.randint(0, 2**48) for _ in range(n)]
    i = [random.randint(1, n) for _ in range(k)]

    ## Sort the array i to process order statistics in order
    i.sort()

    # Cria um dicionário com listas de números de acordo com o tamanho deles
    dict_tamanho = dict_sort(A)
    result = []
    for k in i:
        res = kSelect(dict_tamanho, k)
        result.append(res)

    for res in result:
        print(res, end=" ")


if __name__ == "__main__":
    main()
