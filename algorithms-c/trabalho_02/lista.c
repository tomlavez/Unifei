#include <stdio.h>
#include <stdlib.h>

#include "lista.h"

#define MAX 100

//definição da struct

struct lista
{
  Produto *dados[MAX];
  int qtd;
};

//implementação das funções

//criar lista
Lista* criar_lista(){
  Lista *li = (Lista *)malloc(sizeof(Lista));

  if(li == NULL) return 0;
  
  li->qtd = 0;
  return li;
}

//liberar lista
int liberar_lista(Lista **li)
{
  if (*li == NULL) return 0;
  
  free(*li);
  *li = NULL;

  return 1;
}

//obtem o tamanho da lista
int tamanho_lista(Lista *li)
{
 if(li == NULL) return -1;

 else return li->qtd;
}

//verifica se a lista esta vazia
int lista_vazia(Lista *li)
{
  if(li == NULL) return -1;
  
  if(li->qtd == 0) return 1;
  
  return 0;
}

//verifica se a lista esta cheia
int lista_cheia(Lista *li)
{
  if (li == NULL) return -1;

  if (li->qtd == MAX) return 1;

  return 0;
}

int inserir_lista_inicio(Lista *li, Produto *pro)
{
  if(li == NULL) return 0;

  if(lista_cheia(li) == 1) return 0;
  
  for(int i=li->qtd-1;i>=0;i--)
  {
   li->dados[i+1] = li->dados[i];  
  }
  li->dados[0] = pro;

  li->qtd++;

  return 1;
}

int inserir_lista_final(Lista *li, Produto *pro)
{
  if(li == NULL) return 0;

  if(lista_cheia(li) == 1) return 0;

  li->dados[li->qtd] = pro;
  li->qtd++;

  return 1;
}

Produto* menor_preco(Lista *li)
{
  if(li == NULL) return 0;
  
  float menor = preco_Produto(li->dados[0]);
  int cont = 0;
  
  for(int i=0;i<MAX;i++)
    {
      if (preco_Produto(li->dados[i]) < menor) 
      {
        menor = preco_Produto(li->dados[i]);
        cont = i;
      }
    }
  return li->dados[cont];
}

int remover_ultimos(Lista *li, int n)
{
  if (li == NULL) return 0;
  
  if(lista_vazia(li) == 1) return 0;

  for(int i=0;i<n;i++)
    {
      li->qtd--;
      liberar_Produto(&li->dados[li->qtd]);
      if(lista_vazia(li) == 1) break;
    }
  return 1;
}

int lista_troca(Lista *li, int p1, int p2)
{

  if(li == NULL) return 0;

  if(lista_vazia(li) == 1) return 0;
  
  Produto *pro;
  pro = li->dados[p1-1];
  li->dados[p1-1] = li->dados[p2-1];
  li->dados[p2-1] = pro;
  
  return 1;
}

int lista_imprimir(Lista *li)
{
  if(li == NULL) return 0;

  for(int i=0;i<li->qtd;i++)
    {
      printf("\n%d Produto: ", (i+1));
      printf("\n\tCódigo: %d", codigo_Produto(li->dados[i]));
      printf("\n\tNome: %s", nome_Produto(li->dados[i]));
      printf("\n\tPreço: %.2f", preco_Produto(li->dados[i]));
      printf("\n\tQuantidade: %d item(s)", qtd_Produto(li->dados[i]));
      printf("\n");
    }
  return 1;
}

Produto* lista_Produto(Lista* li, int i)
{
  return li->dados[i];
}