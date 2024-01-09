#include "modulo.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
  Lista *li = NULL;
  int opcao, op2, res, temp, max, min;
  char cidade[30], clima[10];
  Celula *atual = NULL, *anterior = NULL;

  do {
    printf("\n\n################# MENU DE OPCOES #################");
    printf("\n 0 - Sair");
    printf("\n 1 - Criar lista");
    printf("\n 2 - Liberar lista");
    printf("\n 3 - Inserir ordenado por temperatura");
    printf("\n 4 - Remover cidade especifica");
    printf("\n 5 - Buscar informações de uma cidade");
    printf("\n 6 - Editar informações de uma cidade");
    printf("\n 7 - Cidade com a maior temperatura");
    printf("\n 8 - Cidade com a menor temperatura");
    printf("\n 9 - Imprimir lista");
    printf("\n10 - Imprimir lista inteira");
    printf("\nOpção: ");
    scanf("%d", &opcao);

    switch (opcao) {

    case 0:
      liberarLista(li);
      printf("\nFinalizando...\n\n");
      return 0;
      break;
    case 1:
      li = alocarLista();

      if (li != NULL)
        printf("\nLista criada com sucesso!");
      else
        printf("\nLista nao criada!");

      break;
    case 2:
      res = liberarLista(li);
      li = NULL;

      if (res)
        printf("\nLista liberada com sucesso!");
      else
        printf("\nLista nao liberada!");

      break;
    case 3:
      printf("\nDigite a cidade a ser inserida: ");
      scanf(" %[^\n]", cidade);
      printf("Digite a temperatura: ");
      scanf(" %d", &temp);
      printf("Digite a temperatura máxima: ");
      scanf(" %d", &max);
      printf("Digite a temperatura mínima: ");
      scanf(" %d", &min);
      printf("Digite o clima: ");
      scanf(" %[^\n]", clima);
      res = inserirOrdemLista(li, cidade, temp, max, min, clima);

      if (res == 1)
        printf("\nInsercao realizada com sucesso!");
      else
        printf("\n Falha na insercao!");

      break;
    case 4:
      printf("\nDigite a cidade a ser removida: ");
      scanf(" %[^\n]", cidade);
      res = removerEspecifico(li, cidade);

      if (res == 1)
        printf("\nRemocao realizada com sucesso!");
      else
        printf("\nFalha na remocao, elemento nao encontrado!");

      break;
    case 5:
      printf("\nDigite a cidade que deseja buscar: ");
      scanf(" %[^\n]", cidade);
      atual = buscaEspecifico(li, cidade);

      if (atual == NULL) {
        printf("\nCidade não está na lista!");
        break;
      }
      res = imprimirAtual(atual);
      if (res == 0)
        printf("\nLista não encontrada!");

      break;
    case 6:

      printf("\nDigite a cidade que deseja editar: ");
      scanf(" %[^\n]", cidade);
      atual = buscaEspecifico(li, cidade);
      if (atual == NULL) {
        printf("\nCidade não está na lista!");
        break;
      }
      printf("\n------Novas informações------");
      printf("\nDigite a temperatura: ");
      scanf("%d", &temp);
      printf("Digite a temperatura máxima: ");
      scanf("%d", &max);
      printf("Digite a temperatura mínima: ");
      scanf("%d", &min);
      printf("Digite o clima: ");
      scanf(" %[^\n]", clima);
      res = editarCidade(li, cidade, temp, max, min, clima);

      if (res == 1)
        printf("\nEdição realizada com sucesso!");
      else
        printf("\nFalha na edição!");

      break;
    case 7:
      atual = buscaUltimo(li);
      res = imprimirAtual(atual);
      if (res == 0)
        printf("\nLista não encontrada!");

      break;
    case 8:
      atual = buscaPrimeiro(li);
      res = imprimirAtual(atual);
      if (res == 0)
        printf("\nLista não encontrada!");

      break;
    case 9:

      atual = buscaPrimeiro(li);
      anterior = atual;
      res = imprimirAtual(atual);
      if (res == 0)
        printf("\nLista não encontrada!");
      do {
        printf("\n\n#####MENU DE OPÇÕES#####");
        printf("\n\t1 - Próximo elemento");
        printf("\n\t2 - Elemento anterior");
        printf("\n\t3 - Sair");
        printf("\nOpção: ");
        scanf("%d", &op2);

        switch (op2) {

        case 1:

          atual = moverProximo(atual);
          if (anterior == atual) {
            printf("\nElemento não encontrado!");
            break;
          }
          anterior = atual;
          res = imprimirAtual(atual);
          if (res == 0)
            printf("\nLista não encontrada!");

          break;
        case 2:

          atual = moverAnterior(atual);
          if (anterior == atual) {
            printf("\nElemento não encontrado!");
            break;
          }
          anterior = atual;
          res = imprimirAtual(atual);
          if (res == 0)
            printf("\nLista não encontrada!");

          break;
        case 3:

          printf("\nVoltando ao menu principal...");

          break;
        default:

          printf("\nOpção invalida!");
          break;
        }
      } while (op2 != 3);
      break;
    case 10:

      imprimirLista(li);

      break;

    default:
      printf("\nOpcao invalida!");
      break;
    }
  } while (opcao != 0);

  return 0;
}