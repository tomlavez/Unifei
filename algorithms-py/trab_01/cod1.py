# 2023005057 e 2023007893

import random

# essa implementação tem como ideia utilizar o algoritmo quicksort para ordenar a lista
# e a partir disso, utilizar dois ponteiros para encontrar quantos pares na lista somam um valor alvo.


def countingSort(lista):

    # conta quantas vezes cada número aparece na lista e armazena isso em um vetor de contagem
    # a partir disso, cria uma lista de saída, que é preenchido com base na contagem
    # o maior elemento presente no vetor de contagem é o maior, e ultimo, elemento da lista
    # a partir disso, decrementa a contagem e preenche a lista de saída, de trás para frente

    maior = max(lista)
    contagem = [0] * (maior + 1)
    saida = [0] * len(lista)

    for i in lista:
        contagem[i] += 1

    for i in range(1, maior + 1):
        contagem[i] += contagem[i - 1]

    for i in reversed(lista):
        saida[contagem[i] - 1] = i
        contagem[i] -= 1

    return saida


def removerDuplicados(lista):

    # essa função remove duplicatas de uma lista
    # ela cria um dicionário para verificar se um elemento já foi encontrado
    # a partir disso, cria uma nova lista com os elementos únicos

    lista_unica = []
    encontrados = {}

    for elemento in lista:
        if elemento not in encontrados:
            lista_unica.append(elemento)
            encontrados[elemento] = True

    return lista_unica


def buscaPares(alvo, lista):

    # essa função conta quantos pares de números em uma lista ordenada somam alvo
    # começa com dois ponteiros, um no início, no menor valor, e outro no final da lista, no maior valor
    # enquanto os ponteiros não se encontram, verifica se a soma dos elementos apontados por eles é igual ao alvo
    # se for, incrementa o contador e move os ponteiros para o centro
    # se a soma for menor que o alvo, move o ponteiro da esquerda para a direita
    # se a soma for maior que o alvo, move o ponteiro da direita para a esquerda

    contador = 0
    left = 0
    right = len(lista) - 1

    if lista[right] > alvo:
        right -= 1

    while left < right:
        soma = lista[left] + lista[right]
        if soma == alvo:
            contador += 1
            left += 1
            right -= 1
        elif soma < alvo:
            left += 1
        else:
            right -= 1

    return contador


# gera uma lista de tamanho n com números aleatórios
tamanho = 48000
random.seed(tamanho)
l = []

# gera uma lista de tamanho n com números aleatórios
# ordena a lista e remove duplicatas
# repete o processo até que a lista tenha o tamanho desejado
while len(l) < tamanho:
    while len(l) < tamanho:
        num = random.randint(0, 2**17)
        l.append(num)

    l = countingSort(l)
    l = removerDuplicados(l)

# gera um número alvo ímpar
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)

# conta quantos pares de números na lista somam alvo
contador = 0
contador = buscaPares(alvo, l)

print(contador)
