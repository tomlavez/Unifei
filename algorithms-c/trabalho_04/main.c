
// bibliotecas do sistema
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// bibliotecas do projeto
#include "filaEncadeada.h"

// funcao principal
int main(void) {

  // no início a fila está vazia, logo, o ponteiro inicio tem valor NULL
  // o ponteiro inicio conterá o endereço do primeiro elemento da fila
  Fila *xp = NULL;
  Fila *xc = NULL;
  Fila *np = NULL;
  Fila *nc = NULL;
  Fila *se = NULL;

  // definição
  int tipo, perfil, opcao, max = 1, senha;

  // testes
  int teste, ok, i;

  // contagem
  int contX = 0, contN = 0, contPerfil = 0;
  ;

  // menu de opções para execuções de operações sobre a fila
  do {
    printf("\n\nMenu de opções");
    printf("\n1 - Criar filas");
    printf("\n2 - Liberar filas");
    printf("\n3 - Gerar senha");
    printf("\n4 - Chamar senha");
    printf("\n5 - Sair");
    printf("\nOpção: ");
    scanf("%d", &opcao);

    switch (opcao) {

    case 1:

      // criar fila
      xp = criar_fila();
      xc = criar_fila();
      np = criar_fila();
      nc = criar_fila();

      if (xp != NULL && xc != NULL && np != NULL && nc != NULL) {
        printf("\n Digite o limite diario de atendimentos: ");
        scanf(" %d", &max);
        se = criar_fila();
        for (i = 1; i <= max; i++) {
          ok = enfileirar(se, i);
        }

        if (ok != 1) {
          printf("\n Erro na criação de SE!");
        }

      } else {
        printf("\n Filas não criadas!");
      }

      break;

    case 2:

      // liberar fila
      ok = liberar_fila(xp);
      xp = NULL;
      if (ok) {
        ok = liberar_fila(xc);
        xc = NULL;
        if (ok) {
          ok = liberar_fila(np);
          np = NULL;
          if (ok) {
            ok = liberar_fila(nc);
            nc = NULL;
            if (ok) {
              ok = liberar_fila(se);
              se = NULL;
              if (ok) {
                printf("\n Filas liberada com sucesso!");
              } else {
                printf("\n Filas não liberadas!");
              }
            } else {
              printf("\n Filas não liberadas!");
            }
          } else {
            printf("\n Filas não liberadas!");
          }
        } else {
          printf("\n Filas não liberadas!");
        }
      } else {
        printf("\n Fila não liberadas!");
      }
      break;

    case 3:
      // gerar senha

      // consulta se tem alguma senha restante na fila SE
      ok = consultar_inicio_fila(se, &senha);
      if (ok == 0) {
        printf("\n O limité diário de atendimento foi atingido!");

        break;
      }

      // define a fila que vai ter uma senha adicionada
      do {
        printf("\n Qual o tipo de atendimento?\n\t1 - Caixa\t2 - Negocial");
        printf("\n\t Opção: ");
        scanf(" %d", &tipo);
      } while (tipo != 1 && tipo != 2);

      do {
        printf("\n Qual o perfil?\n\t1 - Preferencial\t2 - Convencional");
        printf("\n\t Opção: ");
        scanf(" %d", &perfil);
      } while (perfil != 1 && perfil != 2);

      // adiciona a senha na respectiva fila
      if (tipo == 1 && perfil == 1) {
        ok = enfileirar(xp, senha);
        printf("\n Sua senha é: XP%d", senha);
        printf("\n Fila atual correspondente: ");
        imprimir_fila(xp);
      }

      else if (tipo == 1 && perfil == 2) {
        ok = enfileirar(xc, senha);
        printf("\n Sua senha é: XC%d", senha);
        printf("\n Fila atual correspondente: ");
        imprimir_fila(xc);
      }

      else if (tipo == 2 && perfil == 1) {
        ok = enfileirar(np, senha);
        printf("\n Sua senha é: NP%d", senha);
        printf("\n Fila atual correspondente: ");
        imprimir_fila(np);
      }

      else if (tipo == 2 && perfil == 2) {
        ok = enfileirar(nc, senha);
        printf("\n Sua senha é: NC%d", senha);
        printf("\n Fila atual correspondente: ");
        imprimir_fila(nc);
      }

      if (ok != 1) {
        printf("\n Falha na inserção!");
      }

      // libera a senha adicionada da fila SE
      ok = desenfileirar(se);

      if (ok != 1) {
        printf("\n Falha na remoção de SE!");
      }

      break;

    case 4:
      // chamar senha

      teste = 0;
      // verifica se existem filas vazias
      if (tamanho_fila(nc) + tamanho_fila(np) + tamanho_fila(xc) +
              tamanho_fila(xp) ==
          0) {
        printf("\n Filas estão vazias!");
      } else if (tamanho_fila(nc) + tamanho_fila(np) == 0 &&
                 tamanho_fila(xc) + tamanho_fila(xp) > 0) {
        teste = 2;
      } else if (tamanho_fila(xc) + tamanho_fila(xp) == 0 &&
                 tamanho_fila(nc) + tamanho_fila(np) > 0) {
        teste = 1;
      }
      // se não existir, sorteia uma fila
      else {
        srand(time(NULL));
        teste = (1 + rand() % 2);
      }

      if (teste == 1) { // fila negocial
        i = tamanho_fila(np);
        if (i == 0 ||
            contPerfil == 2) { // verifica se a fila preferencial esta vazia ou
                               // se tiveram duas senhas preferenciais seguidas
          if (contPerfil == 2) {
            contPerfil = 0;
          }
          i = tamanho_fila(nc);
          if (i > 0) { // verifica se a lista convencional esta vazia
            ok = consultar_inicio_fila(nc, &senha);
            if (ok) {
              printf("\n Senha atual: NC%d", senha);
              desenfileirar(nc);
              contN++;
            }
          } else
            printf("\n Filas do atendimento negocial estão vazias!");
        } else {
          ok = consultar_inicio_fila(np, &senha);
          if (ok) {
            printf("\n Senha atual: NP%d", senha);
            contPerfil++;
            desenfileirar(np);
            contN++;
          }
        }
      } else if (teste == 2) { // fila caixa
        i = tamanho_fila(xp);
        if (i == 0 ||
            contPerfil == 2) { // verifica se a fila preferencial esta vazia ou
                               // se tiveram duas senhas preferenciais seguidas
          if (contPerfil == 2) {
            contPerfil = 0;
          }
          i = tamanho_fila(xc);
          if (i > 0) { // verifica se a lista convencional esta vazia
            ok = consultar_inicio_fila(xc, &senha);
            if (ok) {
              printf("\n Senha atual: XC%d", senha);
              desenfileirar(xc);
              contX++;
            }
          } else
            printf("\n Filas dos caixas estão vazias!");
        } else {
          ok = consultar_inicio_fila(xp, &senha);
          if (ok) {
            printf("\n Senha atual: XP%d", senha);
            contPerfil++;
            desenfileirar(xp);
            contX++;
          }
        }
      }

      break;

    case 5:

      // libera memória e finaliza programa
      liberar_fila(xp);
      liberar_fila(xc);
      liberar_fila(np);
      liberar_fila(nc);
      liberar_fila(se);
      printf("\nFinalizando...");
      break;

    default:
      printf("\nOpção inválida!");
      break;
    }

    printf("\n");
    
    if ((contN + contX) == max) {
      ok = consultar_inicio_fila(se, &senha);
      if (ok != 0) {
        printf("\n Fila SE não está vazia");
      }
      ok = consultar_inicio_fila(xp, &senha);
      if (ok != 0) {
        printf("\n Fila XP não está vazia");
      }
      ok = consultar_inicio_fila(xc, &senha);
      if (ok != 0) {
        printf("\n Fila XC não está vazia");
      }
      ok = consultar_inicio_fila(np, &senha);
      if (ok != 0) {
        printf("\n Fila NP não está vazia");
      }
      ok = consultar_inicio_fila(nc, &senha);
      if (ok != 0) {
        printf("\n Fila NC não está vazia");
      }

      printf("\n\nAtendimentos diários realizados!");
      printf("\n\tMesa Negocial: %d atendimentos", contN);
      printf("\n\tMesa Caixa: %d atendimentos", contX);

      break;
    }

  } while (opcao != 5);

  return 0;
}