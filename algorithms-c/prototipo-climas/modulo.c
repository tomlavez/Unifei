#include "modulo.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct cidade {
  char nome[30];
  int temp;
  int maxima;
  int minima;
  char clima[10];
};

struct celula {
  struct celula *ant;
  struct cidade valor;
  struct celula *prox;
};

Celula *alocarCelula() { // criar elemento
  Celula *no = (Celula *)malloc(sizeof(Celula));

  return no;
}

Lista *alocarLista() { // criar lista
  Lista *li = (Lista *)malloc(sizeof(Lista));

  if (li != NULL)
    *li = NULL;

  return li;
}

int liberarLista(Lista *li) {
  if (li == NULL) // verifica se a lista existe
    return 0;

  Celula *no;
  while (*li != NULL) // percorre os nos liberando o ultimo repetidamente
  {
    no = *li;
    *li = (*li)->prox;
    free(no);
  }

  free(li); // libera a cabeca da lista

  return 1;
}

int inserirOrdemLista(Lista *li, char nome[30], int temp, int max, int min,
                      char clima[10]) {
  if (li == NULL) // verifica se a lista existe
    return 0;

  Celula *no = alocarCelula();

  if (no == NULL) // verifica se no foi criado corretamente
    return 0;

  strcpy(no->valor.nome, nome);
  no->valor.temp = temp;
  no->valor.maxima = max;
  no->valor.minima = min;
  strcpy(no->valor.clima, clima);

  if ((*li) == NULL) // se lista vazia, insere no inicio
  {
    no->prox = NULL;
    no->ant = NULL;
    *li = no;
  } else // senao
  {
    Celula *anterior, *atual;
    atual = *li;

    while (atual != NULL && atual->valor.temp < no->valor.temp) {
      anterior = atual;
      atual = atual->prox;
    }

    if (atual == (*li)) {
      no->ant = NULL;
      (*li)->ant = no;
      no->prox = (*li);
      *li = no;
    } else {
      no->prox = anterior->prox;
      no->ant = anterior;
      anterior->prox = no;
      if (atual != NULL) {
        atual->ant = no;
      }
    }
  }

  return 1;
}

int removerEspecifico(Lista *li, char nome[30]) {
  if (li == NULL) // verifica se a lista existe
    return 0;

  if ((*li) == NULL)
    return 0;

  Celula *atual;
  atual = *li;
  int teste = 1;
  char cmp[30];

  while (atual != NULL && teste != 0) {
    strcpy(cmp, atual->valor.nome);
    teste = strcmp(nome, cmp);
    if (teste != 0)
      atual = atual->prox;
  }

  if (atual == NULL)
    return 0;

  if (atual->ant == NULL)
    *li = atual->prox;
  else
    atual->ant->prox = atual->prox;

  if (atual->prox != NULL)
    atual->prox->ant = atual->ant;

  free(atual);
  return 1;
}

int editarCidade(Lista *li, char nome[30], int temp, int max, int min,
                 char clima[10]) {
  Celula *no;
  int teste;

  no = buscaEspecifico(li, nome);

  if (no->ant == NULL && no->prox == NULL) {
    teste = removerEspecifico(li, nome);
    if (teste == 1) {
      teste = inserirOrdemLista(li, nome, temp, max, min, clima);
    }
  } else {
    if (no->ant == NULL) {
      no->prox->ant = NULL;
    }

    if (no->prox == NULL) {
      no->ant->prox = NULL;
    }

    if (no->prox != NULL && no->ant != NULL) {
      no->ant->prox = no->prox;
      no->prox->ant = no->ant;
    }
  }

  teste = removerEspecifico(li, nome);

  if (teste == 1) {
    teste = inserirOrdemLista(li, nome, temp, max, min, clima);
  }
  if (teste != 1)
    return 0;

  return 1;
}

Celula *buscaEspecifico(Lista *li, char nome[30]) {
  if (li == NULL || (*li) == NULL)
    return NULL;

  int teste = 1;

  Celula *no = *li;
  char cmp[30], cmp2[30];

  strcpy(cmp2, nome); // copia o nome para a variavel cmp2

  while (no != NULL && teste != 0) {

    strcpy(cmp, no->valor.nome); // copia nome da cidade para cmp

    teste = strcmp(cmp, cmp2); // compara cmp com cmp2

    if (teste != 0) { // se forem diferentes passa para o prox elemento
      no = no->prox;
    }
  }
  if (no == NULL) // elemento não encontrado
    return 0;

  return no;
}

Celula *buscaUltimo(Lista *li) {
  if (li == NULL || (*li) == NULL) {
    return NULL;
  }

  Celula *no = *li;

  while (no->prox != NULL) {
    no = no->prox;
  }

  return no;
}

Celula *buscaPrimeiro(Lista *li) {
  if (li == NULL || (*li) == NULL) {
    return NULL;
  }

  Celula *no = *li;

  return no;
}

Celula *moverProximo(Celula *dado) {
  if (dado->prox != NULL) {
    dado = dado->prox;
    ;
  }

  return dado;
}

Celula *moverAnterior(Celula *dado) {
  if (dado->ant != NULL) {
    dado = dado->ant;
  }

  return dado;
}

int imprimirAtual(Celula *dado) {
  if (dado == NULL) {
    return 0;
  }

  printf("\nNome: %s ", dado->valor.nome);
  printf("\nTemp: %d ", dado->valor.temp);
  printf("\nMáxima: %d ", dado->valor.maxima);
  printf("\nMínima: %d ", dado->valor.minima);
  printf("\nClima: %s ", dado->valor.clima);
  printf("\n");

  return 1;
}

int imprimirLista(Lista *li) {
  if (li == NULL || (*li) == NULL) {
    printf("\nLista não encontrada!");
    return 0;
  }

  printf("\nLISTA: ");

  Celula *aux = (*li);

  while (aux->prox != NULL) {
    printf("\nNome: %s ", aux->valor.nome);
    printf("\nTemp: %d ", aux->valor.temp);
    printf("\nMáxima: %d ", aux->valor.maxima);
    printf("\nMínima: %d ", aux->valor.minima);
    printf("\nClima: %s ", aux->valor.clima);
    printf("\n");
    aux = aux->prox;
  }

  printf("\nNome: %s ", aux->valor.nome);
  printf("\nTemp: %d ", aux->valor.temp);
  printf("\nMáxima: %d ", aux->valor.maxima);
  printf("\nMínima: %d ", aux->valor.minima);
  printf("\nClima: %s ", aux->valor.clima);

  return 1;
}
