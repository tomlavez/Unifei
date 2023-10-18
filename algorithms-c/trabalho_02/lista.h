#include "produto.h"

typedef struct lista Lista;

//protótipos das funções

//criar lista
Lista* criar_lista();

//libera a lista
int liberar_lista(Lista **li);

//obtem o tamanho da lista
int tamanho_lista(Lista *li);

//verifica se a lista esta vazia
int lista_vazia(Lista *li);

//verifica se a lista esta cheia
int lista_cheia(Lista *li);

//aloca um elemento no início da lista
int inserir_lista_inicio(Lista *li, Produto *pro);

//aloca um elemento no final da lista
int inserir_lista_final(Lista *li, Produto *pro);

//encontra o produto de menor preco
Produto* menor_preco(Lista *li);

//remover ultimos n termos
int remover_ultimos(Lista *li, int n);

//trocar elemento em p1 com o elemento em p2
int lista_troca(Lista *li, int p1, int p2);

//imprimir a lista
int lista_imprimir(Lista *li);

//retorna um elemento da lista
Produto* lista_Produto(Lista* li, int i);