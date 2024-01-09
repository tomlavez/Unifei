#ifndef _MODULO
#define _MODULO

typedef struct celula Celula;
typedef Celula *Lista;

//  gerenciamento
Lista *alocarLista(void);
Celula *alocarCelula(void);
int liberarLista(Lista *li);

//  insercao
int inserirOrdemLista(Lista *li, char nome[30], int temp, int max, int min,
                      char clima[10]);
int editarCidade(Lista *li, char nome[30], int temp, int max, int min,
                 char clima[10]);

//  remocao
int removerEspecifico(Lista *li, char nome[30]);

//  consulta
Celula *buscaEspecifico(Lista *li, char nome[30]);
Celula *buscaPrimeiro(Lista *li);
Celula *buscaUltimo(Lista *li);

// mover
Celula *moverProximo(Celula *dado);
Celula *moverAnterior(Celula *dado);

//  imprimir lista
int imprimirAtual(Celula *dado);
int imprimirLista(Lista *li);

#endif
