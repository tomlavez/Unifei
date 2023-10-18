#include <stdio.h>
#include <stdlib.h>

#include "complex.h"

// definição de struct

struct complex{
  float real;
  float imag;
};

// implementação das funções


//cria um numero complexo
Complex* compCriar(float a, float b)
{
  Complex* p = (Complex*) malloc(sizeof(Complex));
  
  if(!p)
  {
    printf("Memoria insuficiente...\n");
    exit(1);
  }
  
  p->real = a;
  p->imag = b;

  return p;
}

//libera o numero complexo
void compLiberar(Complex* x)
{
  free(x);
}

//soma dois numeros complexos
Complex* compSomar(Complex* a, Complex* b)
{
  Complex* p = (Complex*) malloc(sizeof(Complex));
  
  if(!p)
  {
    printf("Memoria insuficiente...\n");
    exit(1);
  }
  
  p->real = (a->real + b->real);
  p->imag = (a->imag + b->imag);

  return p;
}

//subtrai dois numeros complexos
Complex* compSubtrair(Complex* a, Complex* b)
{
  Complex* p = (Complex*) malloc(sizeof(Complex));
  
  if(!p)
  {
    printf("Memoria insuficiente...\n");
    exit(1);
  }
  
  p->real = (a->real - b->real);
  p->imag = (a->imag - b->imag);

  return p;
}

//multiplica dois numeros complexos
Complex* compMultiplicar(Complex* a, Complex* b)
{
  Complex* p = (Complex*) malloc(sizeof(Complex));
  
  if(!p)
  {
    printf("Memoria insuficiente...\n");
    exit(1);
  }
  
  p->real = ((a->real * b->real) - (a->imag * b->imag));
  p->imag = ((a->imag * b->real) + (a->real * b->imag));

  return p;
}

//divide dois numeros complexos
Complex* compDividir(Complex* a, Complex* b)
{
  Complex* p = (Complex*) malloc(sizeof(Complex));
  
  if(!p)
  {
    printf("Memoria insuficiente...\n");
    exit(1);
  }
  
  p->real = (((a->real * b->real) + (a->imag * b->imag)) / ((b->real * b->real) + (b->imag * b->imag)));
  p->imag = (((a->imag * b->real) - (a->real * b->imag)) / ((b->real * b->real) + (b->imag * b->imag)));


  return p;
}

//imprime um numero complexo
void compImprimir(Complex* a)
{
    printf("%.2f + %.2fi", a->real, a->imag);
}