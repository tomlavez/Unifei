typedef struct complex Complex;

//protótipos das funções

//função para criar um numero complexo
Complex* compCriar(float a, float b);

//função para liberar a memoria de um numero complexo
void compLiberar(Complex* x);

//função para somar dois numeros complexos
Complex* compSomar(Complex* a, Complex* b);

//função para subtrair dois numeros complexos
Complex* compSubtrair(Complex* a, Complex* b);

//função para multiplicar dois numeros complexos
Complex* compMultiplicar(Complex* a, Complex* b);

//função para dividir dois numeros complexos
Complex* compDividir(Complex* a, Complex* b);

//função para imprimir o valor de um numero complexo
void compImprimir(Complex* a);