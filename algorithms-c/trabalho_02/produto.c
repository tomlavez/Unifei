#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "produto.h"

struct produto
{
  int codigo;
  char nome[30];
  float preco;
  int qtd;
};

Produto* criar_Produto(int codigo, char nome[30], float preco, int qtd)
{
  Produto *pro = (Produto *)malloc(sizeof(Produto));

  if(pro == NULL) return 0;

  pro->codigo = codigo;
  strcpy(pro->nome, nome);
  pro->preco = preco;
  pro->qtd = qtd;

  return pro;
}
 
int imprimir_Produto(Produto *pro){

  if(pro == NULL) return 0;
  
  printf("\n\t%d", pro->codigo);
  printf("\n\t %s", pro->nome);
  printf("\n\t%f", pro->preco);
  printf("\n\t%d item(s)", pro->qtd);

  return 1;
}

int liberar_Produto(Produto **pro)
{
  if (*pro == NULL) return 0;

  free(*pro);
  *pro = NULL;

  return 1;
}

int codigo_Produto(Produto *pro)
{
  return pro->codigo;
}

char* nome_Produto(Produto *pro)
{
  return pro->nome;
}

float preco_Produto(Produto *pro)
{
  return pro->preco;
}

int qtd_Produto(Produto *pro)
{
  return pro->qtd;
}