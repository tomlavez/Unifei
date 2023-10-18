
// bibliotecas do sistema
#include <stdio.h>

// bibliotecas do projeto
#include "listaEncadeadaCircular.h"

int criar_dado(int *dado);

// funcao principal
int main(void) {

  // no início a lista está vazia, logo, o ponteiro inicio tem valor NULL
  // o ponteiro inicio conterá o endereço do primeiro elemento da lista
  Lista *li = NULL, *l2 = NULL, *l3 = NULL, *l4 = NULL;
  int opcao, dado, ok, pos;

  // criar e preencher a segunda lista
  li = criar_lista();

  inserir_lista_final(li, 6);
  inserir_lista_final(li, 5);
  inserir_lista_final(li, 4);
  inserir_lista_final(li, 3);
  inserir_lista_final(li, 2);
  inserir_lista_final(li, 1);
  
  l2 = criar_lista();

  inserir_lista_final(l2, 5);
  inserir_lista_final(l2, 6);
  inserir_lista_final(l2, 7);
  inserir_lista_final(l2, 8);
  inserir_lista_final(l2, 9);
  inserir_lista_final(l2, 10);

  l3 = criar_lista();

  l4 = criar_lista();

  inserir_lista_final(l4, 4);
  inserir_lista_final(l4, 4);
  inserir_lista_final(l4, 4);
  inserir_lista_final(l4, 4);
  inserir_lista_final(l4, 4);
  inserir_lista_final(l4, 4);
  

  // menu de opções para execuções de operações sobre a lista
  do {
    printf("\n\nMenu de opções");
    printf("\n1 - Criar lista");
    printf("\n2 - Liberar lista");
    printf("\n3 - Inserir elemento no início");
    printf("\n4 - Inserir elemento no final");
    printf("\n5 - Inserir elemento (ordenado)");
    printf("\n6 - Remover elemento do início");
    printf("\n7 - Remover elemento do final");
    printf("\n8 - Remover elemento (qualquer)");
    printf("\n9 - Buscar elemento pela posição");
    printf("\n10 - Buscar elemento pelo dado");
    printf("\n11 - Imprimir lista");
    printf("\n12 - Concatenar lista");
    printf("\n13 - Eliminar valores repetidos da lista");
    printf("\n14 - Inverter lista");
    printf("\n15 - Verificar se a lista está ordenada");
    printf("\n16 - Tamanho da lista");
    printf("\n17 - Sair");
    printf("\nOpção: ");
    scanf("%d", &opcao);
    switch (opcao) {

    case 1:

      // criar lista
      li = criar_lista();

      if (li != NULL) {
        printf("\nLista criada com sucesso!");
      } else {
        printf("\nLista não criada!");
      }
      break;

    case 2:

      // liberar lista
      ok = liberar_lista(li);
      li = NULL;

      if (ok) {
        printf("\nLista liberada com sucesso!");
      } else {
        printf("\nLista não liberada!");
      }
      break;

    case 3:

      // inserir elemento no início
      ok = criar_dado(&dado);
      ok = inserir_lista_inicio(li, dado);

      if (ok == 1) {
        printf("\nInserção realizada com sucesso!");
      } else {
        printf("\nFalha na inserção!");
      }

      break;

    case 4:

      // inserir elemento no final
      ok = criar_dado(&dado);
      ok = inserir_lista_final(li, dado);

      if (ok == 1) {
        printf("\nInserção realizada com sucesso!");
      } else {
        printf("\nFalha na inserção!");
      }

      break;

    case 5:

      // inserir elemento de forma ordenada
      ok = criar_dado(&dado);
      ok = inserir_lista_ordenada(li, dado);

      if (ok == 1) {
        printf("\nInserção realizada com sucesso!");
      } else {
        printf("\nFalha na inserção!");
      }

      break;

    case 6:

      // remover elemento do início
      ok = remover_lista_inicio(li);

      if (ok == 1) {
        printf("\nRemoção realizada com sucesso!");
      } else {
        printf("\nFalha na remoção!");
      }
      break;

    case 7:

      // remover elemento do final
      ok = remover_lista_final(li);

      if (ok == 1) {
        printf("\nRemoção realizada com sucesso!");
      } else {
        printf("\nFalha na remoção!");
      }
      break;

    case 8:

      // remover elemento do meio
      printf("\nCódigo a ser removido: ");
      scanf("%d", &dado);

      ok = remover_lista_meio(li, dado);

      if (ok == 1) {
        printf("\nRemoção realizada com sucesso!");
      } else {
        printf("\nFalha na remoção!");
      }
      break;

    case 9:

      // busca elemento pela posicao
      printf("\nPosição do elemento a ser buscado: ");
      scanf("%d", &pos);

      ok = buscar_lista_posicao(li, pos, &dado);

      if (ok) {
        printf("\nBusca realizada com sucesso!");
        printf("\nElemento da %dª posição: ", pos);
        printf("%d", dado);
      } else {
        printf("\nPosição não existe!");
      }

      break;

    case 10:

      // busca elemento pelo dado
      printf("\nCódigo a ser buscado: ");
      scanf("%d", &dado);

      ok = buscar_lista_dado(li, dado, &pos);

      if (ok) {
        printf("\nBusca realizada com sucesso!");
        printf("\nElemento com código %d na lista: ", dado);
        printf("%d", pos);
      } else {
        printf("\nElemento não encontrado!");
      }

      break;

    case 11:

      // imprime a lista
      printf("\nLista encadeada circular: ");
      ok = imprimir_lista(li);

      break;

    case 12:

      //concatena as listas
      ok = concatenar_lista(li, l4);

      if (ok == -1)
        printf ("\nErro...");
      else if (ok == 0)
        printf("\nListas vazias...");
      else
        printf("\nListas concatenadas!");

      break;

    case 13:

      //elimina elementos repetidos
      ok = eliminar_repetidos_lista(li, l3);
      if (ok == 0) 
      printf("\nErro...");
      else{
        printf("\nLista sem elementos repetidos: ");
        ok = imprimir_lista(l3);
      }
      
      break;

    case 14:

      //inverte a lista
      ok = inverter_lista(li, l3);
      if(ok == 0)
        printf("\nErro...");
      else{
        printf("\nLista invertida: ");
        ok = imprimir_lista(l3);
      }
      break;

    case 15:

      //verifica se a lista está ordenada
      ok = 0;
      ok = verificar_lista_ordenada(li);

      switch (ok) {
      case -1:
        printf("\nA lista está vazia.");
        break;

      case 0:
        printf("\nA lista não está ordenada.");
        break;

      case 1:
        printf("\nA lista está em ordem crescente.");
        break;

      case 2:
        printf("\nA lista está em ordem decrescente.");
        break;

      default:
        printf("\nErro...");
      }

      break;

    case 16:

      //verifica o tamanho da lista
      ok = tamanho_lista(li);
      if (ok == 0)
        printf("Erro...");
      else
        printf("\nA lista tem %d elementos.", ok);
      
      break;
      
    case 17:

      liberar_lista(li);
      liberar_lista(l2);
      liberar_lista(l3);

      printf("\nFinalizando...");
      break;

    default:
      printf("\nOpção inválida!");
      break;
    }

  } while (opcao != 17);

  return 0;
}

int criar_dado(int *dado) {
  printf("\nDigite um valor: ");
  scanf("%d", dado);

  return 1;
}