typedef struct produto Produto;

//prototipos das funcoes

//cria um produto
Produto* criar_Produto(int codigo, char nome[30], float preco, int qtd);

//imprime um produto
int imprimir_Produto(Produto *pro);

//libera o produto
int liberar_Produto(Produto **pro);

//retorna o codigo do produto
int codigo_Produto(Produto *pro);

//retorna o nome do produto
char* nome_Produto(Produto *pro);

//retorna o preço do produto
float preco_Produto(Produto *pro);

//retorna a quantidade de produto
int qtd_Produto(Produto *pro);