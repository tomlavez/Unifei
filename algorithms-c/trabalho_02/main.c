#include <stdio.h>
#include <stdlib.h>

#include "lista.h"

int main(void) {

  Lista *li = NULL;
  int opcao, ok, qtd, codigo, qtd2;
  char nome[50];
  float preco;
  Produto *x;
  
  do{
    printf("\n\nMenu de opções");
    printf("\n1 - Criar lista");
    printf("\n2 - Liberar lista");
    printf("\n3 - Obter o tamanho da lista");
    printf("\n4 - Inserir elemento no início");
    printf("\n5 - Inserir elemento no final");
    printf("\n6 - Remover elementos do final");
    printf("\n7 - Trocar dois elementos de posição");
    printf("\n8 - Buscar o elemento de menor preço");
    printf("\n9 - Imprimir lista");
    printf("\n10 - Sair");
    printf("\nOpção: ");
    scanf("%d", &opcao);

    switch(opcao){

      case 1:

        //criar lista
        li = criar_lista();

        if(li != NULL) printf("\nLista criada com sucesso!");
        else printf("\nLista não criada!!");
        break;

    case 2:

      //liberar lista
      ok = liberar_lista(&li);
      
      if(ok == 0)
      {
        printf("\nFalha na busca...");
        break;
      }

      else if (ok == 1)
      {
        printf("\nLista liberada com sucesso! %p", li);
        break;
      }
        
      else
      {
      printf("\nLista não liberada!");
      break;
      }
        
    case 3:

      //obter o tamanho da lista
      ok = tamanho_lista(li);

      if(ok == -1)
      {
        printf("\nFalha na busca...");
        break;
      }
      
      else printf("\nA lista possui %d produtos", ok);
      
      break;

    case 4:

      if(lista_vazia(li) == -1)
      {
        printf("\nFalha na busca...");
        break;
      }
      
      //inserir elemento no início
      printf("\nDigite o código do produto: ");
      scanf("%d", &codigo);
      printf("Digite o nome do produto: ");
      scanf(" %[^\n]", nome);
      printf("Digite o preco do produto: ");
      scanf("%f", &preco);
      printf("Digite a quantidade de produto: ");
      scanf("%d", &qtd);
      x = criar_Produto(codigo, nome, preco, qtd);
      ok = inserir_lista_inicio(li, x);
      
      if(ok == 1) printf("\nInserção realizada com sucesso!");
      else printf("\nFalha na inserção!");
      break;

    case 5:

      if(lista_vazia(li) == -1)
      {
        printf("\nFalha na busca...");
        break;
      }
      
      //inserir elemento no final
      printf("\nDigite o código do produto: ");
      scanf("%d", &codigo);
      printf("Digite o nome do produto: ");
      scanf(" %[^\n]", nome);
      printf("Digite o preco do produto: ");
      scanf("%f", &preco);
      printf("Digite a quantidade de produto: ");
      scanf("%d", &qtd);
      x = criar_Produto(codigo, nome, preco, qtd);
      ok = inserir_lista_final(li, x);
      
      if(ok == 1) printf("\nInserção realizada com sucesso!");
      else printf("\nFalha na inserção!");
      
      break;

    case 6:

      if(lista_vazia(li) == -1)
      {
        printf("\nFalha na busca...");
        break;
      }
      
      //remover elementos do final da lista
      printf("\nQuantos elementos deseja remover? ");
      scanf("%d", &qtd);

      ok = remover_ultimos(li, qtd);

      if(ok == 1) printf("\nRemoção realizada com sucesso!");
      else printf("\nFalha na remoção...");

      break;
      
    case 7:

      if(lista_vazia(li) == -1)
      {
        printf("\nFalha na busca...");
        break;
      }
      
      //trocar elementos da lista
      printf("\nQuais elementos deseja trocar? ");
      scanf("%d %d", &qtd, &qtd2);

      ok = lista_troca(li, qtd, qtd2);

      if(ok == 1) printf("\nTroca realizada com sucesso!");
      else printf("\nFalha na troca...");

      break;

    case 8:

      //buscar elemento de menor preço
      x = menor_preco(li);
      ok  = imprimir_Produto(x);
      printf("%d", ok);

      if(ok != 1) printf("\nFalha na busca...");

      break;

    case 9:

      //imprime a lista
      ok = lista_imprimir(li);

      if(ok != 1) printf("\nFalha na busca...");

      break;


    case 10:

      //libera a memória e finaliza o programa
      liberar_lista(&li);

      printf("\nFinalizando...");
      break;

    default:

      printf("Opção inválida!");
      break;
    }
  
  }while(opcao != 10);
  
  return 0;
}