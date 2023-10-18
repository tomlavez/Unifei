// TAD para Lista Dinâmica Encadeada Circular baseado no livro "Estrutura de
// dados descomplicada em lingugem C (André Backes)"

#include "listaEncadeadaCircular.h"
#include <stdio.h>
#include <stdlib.h>

// definição do struct elemento
typedef struct elemento {
  int dado;
  struct elemento *prox;
} Elemento;

//**************************************************************************
// função para alocar memória do tipo Lista
Lista *criar_lista() {
  // 'li' é um ponteiro para ponteiro do tipo Elemento
  Lista *li = (Lista *)malloc(sizeof(Lista));

  // se a alocação estiver correta 'li' aponta para NULL (lista vazia)
  if (li != NULL) {
    *li = NULL;
  } else {
    return NULL;
  }

  return li;
}

//**************************************************************************
// função para liberar memória
int liberar_lista(Lista *li) {
  // verifica se a lista foi alocada corretamente
  if (li == NULL) {
    return 0;
  }

  // verifica se a lista não está vazia
  if ((*li) != NULL) {
    Elemento *no, *aux;
    no = *li;

    // laço percorre a lista até o último elemento, liberando o anterior
    while (no->prox != (*li)) {
      aux = no;
      no = no->prox;
      free(aux);
    }

    // libera o último elemento
    free(no);

    // libera o ponteiro de ponteiro (Lista)
    free(li);
  }

  return 1;
}

//**************************************************************************
// função para obter o tamanho da lista
int tamanho_lista(Lista *li) {
  // verifica se a lista foi alocada corretamente ou se a lista está vazia
  if (li == NULL || (*li) == NULL) {
    return 0;
  }

  // inicializa o contador de elementos
  int cont = 0;

  // cria um ponteiro do tipo Elemento que aponta para o primeiro elemento da
  // lista
  Elemento *no;
  no = *li;

  // incrementa 'cont' até acabar o último elemento da lista
  do {
    cont++;
    no = no->prox;
  } while (no != (*li));

  // retorna a quantidade de elementos da lista
  return cont;
}

//**************************************************************************
// função para verificar se a lista está vazia
int lista_vazia(Lista *li) {
  // verifica se houve problema na criação da lista
  // ou seja, 'li' não é uma lista válida
  if (li == NULL) {
    return -1;
  }

  // verifica se a lista foi criada corretamente
  // mas não contém nenhum valor (lista vazia)
  if (*li == NULL) {
    return 1;
  }

  // se houver elementos, retorna 0
  return 0;
}

// função para alocar memória do tipo Elemento
Elemento *criar_elemento() {
  // 'no' é um ponteiro do tipo Elemento
  Elemento *no = (Elemento *)malloc(sizeof(Elemento));

  // retorna ponteiro alocado
  return no;
}

// função para inserir elemento no início da lista
int inserir_lista_inicio(Lista *li, int dado) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  // cria um elemento novo ('no' precisa ser alocado pois estamos inserindo ele
  // na lista)
  Elemento *no;
  no = criar_elemento();

  // verifica se a memória foi alocada corretamente
  if (no == NULL) {
    return 0;
  }

  // atribui valores ao elemento novo
  no->dado = dado;

  // verifica se a lista está vazia
  if ((*li) == NULL) {

    // insere elemento único no início da lista
    no->prox = no; // próximo elemento na lista circular é ele mesmo
    *li = no;      // 'no' passa a ser o primeiro elemento da lista

  } else {

    Elemento *aux;
    aux = *li;

    // percorre a lista até o último elemento
    while (aux->prox != (*li)) {
      aux = aux->prox;
    }

    // insere elemento no início da lista
    aux->prox = no; // 'no' é o próximo elemento na lista circular após o último
    no->prox = *li; // primeiro elemento antigo '*li' é o próximo após o 'no'
    *li = no;       // 'no' passa a ser o primeiro elemento
  }

  return 1;
}

// função para inserir elemento no final da lista
int inserir_lista_final(Lista *li, int dado) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  // cria um elemento novo ('no' precisa ser alocado pois estamos inserindo ele
  // na lista)
  Elemento *no;
  no = criar_elemento();

  // verifica se a memória foi alocada corretamente
  if (no == NULL) {
    return 0;
  }

  // atribui valores ao elemento novo
  no->dado = dado;

  // verifica se a lista está vazia
  if ((*li) == NULL) {

    // insere elemento único no início da lista
    no->prox = no; // próximo elemento na lista circular é ele mesmo
    *li = no;      // 'no' passa a ser o primeiro elemento da lista

  } else {

    Elemento *aux;
    aux = *li;

    // percorre a lista até o último elemento
    while (aux->prox != (*li)) {
      aux = aux->prox;
    }

    // insere elemento no final da lista
    aux->prox = no; // 'no' é o próximo elemento na lista circular após o último
    no->prox = *li; // primeiro elemento '*li' é o próximo após o 'no'
  }

  return 1;
}

// função para inserir elemento na lista de forma ordenada
int inserir_lista_ordenada(Lista *li, int dado) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  // cria um elemento novo ('no' precisa ser alocado pois estamos inserindo ele
  // na lista)
  Elemento *no;
  no = criar_elemento();

  // verifica se a memória foi alocada corretamente
  if (no == NULL) {
    return 0;
  }

  // atribui valores ao elemento novo
  no->dado = dado;

  // verifica se a lista está vazia
  if ((*li) == NULL) {

    // insere elemento único no início da lista
    no->prox = no; // próximo elemento na lista circular é ele mesmo
    *li = no;      // 'no' passa a ser o primeiro elemento da lista

  } else {

    // primeira posição é a correta para inserção do elemento novo
    if ((*li)->dado > dado) {

      Elemento *aux;
      aux = *li;

      // percorre a lista até o último elemento
      while (aux->prox != (*li)) {
        aux = aux->prox;
      }

      // insere elemento no início da lista
      aux->prox =
          no; // 'no' é o próximo elemento na lista circular após o último
      no->prox = *li; // primeiro elemento antigo '*li' é o próximo após o 'no'
      *li = no;       // 'no' passa a ser o primeiro elemento
    }

    // senão, percorre a lista, a partir do segundo elemento, até achar o local
    // correto e insere
    Elemento *anterior, *atual;

    anterior = *li;
    atual = anterior->prox;

    // percorre a lista até o último elemento ou até encontrar um elemento maior
    // que o novo
    while (atual != (*li) && atual->dado < dado) {
      anterior = atual;
      atual = atual->prox;
    }

    // insere elemento na posição correta da lista (meio)
    anterior->prox =
        no; // 'no' é o próximo elemento na lista circular após o anterior
    no->prox = atual; // 'atual' é o próximo elemento após o 'no'
  }

  return 1;
}

// função para remover elemento do início da lista
int remover_lista_inicio(Lista *li) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  // verifica se a lista está vazia (não existem elementos a serem removidos)
  if ((*li) == NULL) {
    return 0;
  }

  // verifica se existe apenas um elemento na lista (após remoção a lista fica
  // vazia)
  if ((*li)->prox == (*li)) {

    // libera elemento único
    free(*li);
    // indica que a lista ficou vazia
    *li = NULL;

    return 1;
  }

  Elemento *atual, *aux;
  atual = *li; // 'no' é o elemento a ser removido
  aux = *li;

  // percorre a lista até o último elemento
  while (aux->prox != (*li)) {
    aux = aux->prox;
  }

  // remove o primeiro elemento da lista
  aux->prox = atual->prox; // 'no->prox' é o próximo elemento na lista circular
                           // após o último
  *li =
      atual->prox; // primeiro elemento da lista '*li' passa a ser o 'no->prox'

  // libera Elemento 'no'
  free(atual);

  return 1;
}

// função para remover elemento do final da lista
int remover_lista_final(Lista *li) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  // verifica se a lista está vazia (não existem elementos a serem removidos)
  if ((*li) == NULL) {
    return 0;
  }

  // verifica se existe apenas um elemento na lista (após remoção a lista fica
  // vazia)
  if ((*li)->prox == (*li)) {

    // libera elemento único
    free(*li);

    // indica que a lista ficou vazia
    *li = NULL;

    return 1;
  }

  Elemento *anterior, *atual;
  atual = *li; // 'no' é o elemento a ser removido

  // percorre a lista até 'no' ser o último elemento, armazenando o elemento
  // anterior
  while (atual->prox != (*li)) {
    anterior = atual;
    atual = atual->prox;
  }

  // remove o último elemento da lista
  anterior->prox = atual->prox; // 'no->prox' passa a ser o próximo elemento na
                                // lista circular após o 'anterior'

  // libera Elemento 'no'
  free(atual);

  return 1;
}

// função para remover elemento do meio da lista
int remover_lista_meio(Lista *li, int dado) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  // verifica se a lista está vazia (não existem elementos a serem removidos)
  if ((*li) == NULL) {
    return 0;
  }

  Elemento *atual;
  Elemento *anterior;

  atual = *li;

  // elemento a ser removido está no início da lista
  if (atual->dado == dado) {

    // verifica se existe apenas um elemento na lista (após remoção a lista fica
    // vazia)
    if (atual->prox == atual) {

      // indica que a lista ficou vazia e remove o 'no'
      *li = NULL;
      free(atual);

      // libera Elemento 'no'
      return 1;

      // remove o primeiro elemento
    } else {

      anterior = *li;

      // percorre a lista até o último elemento
      while (anterior->prox != (*li)) {
        anterior = anterior->prox;
      }

      // remove primeiro elemento 'no' (no = *li)
      anterior->prox = atual->prox;
      *li = atual->prox;

      // libera Elemento 'no'
      free(atual);

      return 1;
    }
  }

  anterior = atual;
  atual = atual->prox;

  // percorre a lista até achar o elemento a ser removido, ou até encontrar o
  // primeiro elemento
  while (atual != (*li) && atual->dado != dado) {
    anterior = atual;
    atual = atual->prox;
  }

  // elemento a ser removido não foi encontrado
  if (atual == (*li)) {
    return 0;
  }

  // remove o elemento 'no'
  anterior->prox = atual->prox; // 'no->prox' passa a ser o próximo elemento na
                                // lista circular após o 'anterior'

  // libera Elemento 'no'
  free(atual);

  return 1;
}

// função para buscar o elemento que está na posição 'pos' (primeiro elemento
// está na posição '1')
int buscar_lista_posicao(Lista *li, int pos, int *dado) {
  // verifica se a lista foi criada corretamente, se está vazia ou se a posição
  // 'pos' é inválida
  if (li == NULL || (*li) == NULL || pos <= 0) {
    return 0;
  }

  Elemento *no = *li;
  int i = 1;

  // percorre a lista até achar posicao desejada, ou até encontrar o último
  // elemento
  while (no->prox != (*li) && i < pos) {
    no = no->prox;
    i++;
  }

  // verifica se a posicao desejada existe na lista
  if (i != pos) {
    return 0;

  } else {
    // copia o dado da posição desejada (parâmetro passado por referência)
    *dado = no->dado;
    return 1;
  }
}

// função para buscar o elemento "dado"
int buscar_lista_dado(Lista *li, int dado, int *pos) {
  // verifica se a lista foi criada corretamente ou se está vazia
  if (li == NULL || (*li) == NULL) {
    return 0;
  }

  Elemento *no = *li;
  int i = 1;

  // percorre a lista até achar o elemento desejado, ou até encontrar o último
  // elemento
  while (no->prox != (*li) && no->dado != dado) {
    no = no->prox;
    i++;
  }

  // verifica se dado procurado existe na lista
  if (no->dado != dado) {
    return 0;

  } else {
    // copia a posição da lista onde o dado foi encontrado (parâmetro passado
    // por referência)
    *pos = i;
    return 1;
  }
}

int imprimir_lista(Lista *li) {
  // verifica se a lista foi criada corretamente
  if (li == NULL) {
    return 0;
  }

  if ((*li) == NULL) {
    printf(" Lista vazia!");
  }

  // imprime primeiro elemento
  Elemento *no;
  no = (*li);

  // percorre lista até o último elemento
  while (no->prox != (*li)) {
    printf(" %d ", no->dado);
    no = no->prox;
  }

  // imprime último elemento
  printf(" %d ", no->dado);

  return 1;
}

// concatena duas listas
int concatenar_lista(Lista *l1, Lista *l2) {
  // verifica se as listas foram criadas corretamentes
  if (l1 == NULL && l2 == NULL)
    return -1;

  // verifica se as listas possuem algum valor para ser concatenado
  if (*l1 == NULL && *l2 == NULL)
    return 0;

  // lista 1 vazia

  Elemento *aux1;

  if (*l1 == NULL) {
    *l1 = *l2;
    aux1 = *l2;
    while ((aux1)->prox != (*l2)) {
      (aux1 = aux1->prox);
    }
    aux1->prox = (*l1);
    *l2 = NULL;
    liberar_lista(l2);
    return 1;
  }

  // lista 1 não vazia, busca o ultimo elemento para concatenar

  Elemento *aux2, *aux3;
  aux2 = (*l1);
  aux3 = (*l2);

  while (aux2->prox != (*l1)) {
    aux2 = aux2->prox;
  }

  aux2->prox = *l2;

  if ((*l2) == NULL) {
    *l2 = *l1;
  } else {
    while (aux3->prox != (*l2)) {
      aux3 = aux3->prox;
    }
    aux3->prox = *l1;
  }

  *l2 = NULL;
  liberar_lista(l2);

  return 1;
}

// elimina valores repetidos de l1 e armazena a nova lista em l2
int eliminar_repetidos_lista(Lista *l1, Lista *l2) {

  // verifica se as listas foram criadas corretamentes
  if (l1 == NULL || l2 == NULL || *l1 == NULL)
    return 0;

  // esvazia l2
  if ((*l2) != NULL) {

    Elemento *aux, *no;
    no = *l2;

    while (no->prox != (*l2)) {
      aux = no;
      no = no->prox;
      free(aux);
    }

    free(no);
    *l2 = NULL;
  }

  // preenche l2 com os valores de l1
  Elemento *aux1;
  int cont, ok;

  aux1 = (*l1);

  if ((*l2) == NULL) {
    inserir_lista_final(l2, aux1->dado);
    aux1 = aux1->prox;
  }

  do {
    cont = 0;
    ok = buscar_lista_dado(l2, aux1->dado, &cont); // procura o dado em l2 e,
    if (ok == 0) {                                 // se não achar, retorna 0
      inserir_lista_final(l2, aux1->dado);
    }
    aux1 = aux1->prox;
  } while (aux1 != (*l1));

  return 1;
}

// inverte a lista l1 e armazena em l2
int inverter_lista(Lista *l1, Lista *l2) {

  if (l1 == NULL || l2 == NULL || *l1 == NULL)
    return 0;

  // esvazia a lista l2
  if ((*l2) != NULL) {

    Elemento *aux, *no;
    no = *l2;

    while (no->prox != (*l2)) {
      aux = no;
      no = no->prox;
      free(aux);
    }

    free(no);
    *l2 = NULL;
  }

  // inverte l1 e armazena em l2
  Elemento *anterior, *aux;
  int cont;

  aux = (*l1);

  do {
    inserir_lista_inicio(l2, aux->dado);
    aux = aux->prox; // ultimo elemento
  } while (aux != (*l1));

  return 1;
}

// verifica se a lista está ordenada. Retorna 1 se estiver em ordem crescente, 2
// se estiver em ordem decrescente e 0 se não estiver ordenada
int verificar_lista_ordenada(Lista *l1) {

  if (l1 == NULL)
    return 123;

  if ((*l1) == NULL) {
    return -1;
  }

  Elemento *anterior, *aux;
  int teste = 0;

  // verificar se a lista esta ordenada crescente
  aux = (*l1);
  anterior = aux;

  do {
    aux = aux->prox;
    if (anterior->dado > aux->dado) {
      teste++;
    }

    anterior = aux;

    if (teste != 0) {
      break;
    }
  } while (aux->prox != (*l1));

  if (teste == 0)
    return 1;

  // verificar se a lista esta ordenada em ordem decrescente
  else {
    aux = *l1;
    anterior = aux;
    teste = 0;

    do {
      aux = aux->prox;
      if (anterior->dado < aux->dado) {
        teste++;
      }

      anterior = aux;

      if (teste != 0) {
        break;
      }
    } while (aux->prox != (*l1));

    if (teste == 0)
      return 2;

    // retorna que a lista não esta ordenada
    else
      return 0;
  }
}