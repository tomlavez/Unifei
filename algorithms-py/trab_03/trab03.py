# 2023005057 e 2023007893

import csv


class Noh:
    def __init__(self, pergunta=None, esq=None, dir=None, elemento=None):
        self.pergunta = pergunta  # Pergunta associada ao nó
        self.esq = esq  # Subárvore para a resposta "sim"
        self.dir = dir  # Subárvore para a resposta "não"
        self.elemento = elemento  # Elemento se for um nó folha


def construir_arvore(elementos, perguntas):
    # Se houver apenas um elemento, retorna um nó folha com o elemento
    if len(elementos) == 1:
        return Noh(elemento=elementos[0][0])

    melhor_pergunta = None
    menor_diferenca = None

    # Iterar sobre todas as perguntas possíveis
    for i in range(1, len(perguntas) + 1):
        esq = []
        dir = []

        for elem in elementos:
            if elem[i] == "1":
                esq.append(elem)
            else:
                dir.append(elem)

        # Calcular a diferença entre respostas "sim" e "não"
        diferenca = abs(len(esq) - len(dir))

        # Escolher a pergunta que minimiza a diferença ou a primeira em caso de empate
        if (
            menor_diferenca is None
            or diferenca < menor_diferenca
            or (diferenca == menor_diferenca and (melhor_pergunta is None))
        ):
            menor_diferenca = diferenca
            melhor_pergunta = i

    # Recursivamente construir subárvores para as respostas "sim" e "não"
    esq_elementos = []
    dir_elementos = []

    # Separar elementos para as respostas "sim" e "não"
    for elem in elementos:
        if elem[melhor_pergunta] == "1":
            esq_elementos.append(elem)
        else:
            dir_elementos.append(elem)

    # Constroi as subárvores recursivamente
    esq_subarvore = construir_arvore(esq_elementos, perguntas)
    dir_subarvore = construir_arvore(dir_elementos, perguntas)

    return Noh(perguntas[melhor_pergunta - 1], esq_subarvore, dir_subarvore)


def calcular_altura_media(raiz):
    # Inicializa variáveis para armazenar a soma das alturas e o número de elementos
    total_altura = 0
    total_elementos = 0

    fila = [(raiz, 0)]  # Inicializa a fila com a raiz e a altura 0

    # Enquanto houver elementos na fila
    while fila:
        nodo, altura = fila[0]  # Obtém o primeiro elemento da fila
        fila.pop(0)  # Remove o primeiro elemento da fila

        # Verifica se é um nó folha
        if nodo.elemento:
            # Se for um nó folha, adiciona sua altura à soma total de alturas e incrementa o número de elementos
            total_altura += altura
            total_elementos += 1

        # Senão, adiciona filhos à fila, incrementando a altura
        else:
            if nodo.esq:
                fila.append((nodo.esq, altura + 1))
            if nodo.dir:
                fila.append((nodo.dir, altura + 1))

    # Calcula a média das alturas se houver elementos folha, senão retorna 0
    if total_elementos > 0:
        return total_altura / total_elementos
    else:
        return 0


def main():
    nome_arquivo = input()  # Lê o nome do arquivo CSV
    file = open(nome_arquivo, "r")  # Abre o arquivo CSV

    linhas = csv.reader(file)  # Lê os dados do arquivo CSV
    dados = list(linhas)  # Converte os dados em uma lista de listas

    perguntas = dados[0][1:]  # Extrai as perguntas da primeira linha

    # Extrai os elementos dos dados
    elementos = []

    for linha in dados[1:]:
        elementos.append(linha)

    # Constrói a árvore de decisão e calcula a altura média
    arvore = construir_arvore(elementos, perguntas)
    altura_media = calcular_altura_media(arvore)

    # Imprime a altura média com duas casas decimais
    print(f"{altura_media:.2f}")


if __name__ == "__main__":
    main()
