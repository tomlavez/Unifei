#include <stdio.h>
#include <stdlib.h>

#include "complex.h"

int main()
{
  Complex *n1, *n2, *soma, *sub, *multi, *div;

  n1 = compCriar(4, 4);
  n2 = compCriar(2, 2);

  soma = compSomar(n1, n2);
  printf("\nSoma dos numeros complexos = ");
  compImprimir(soma);
  
  sub = compSubtrair(n1, n2);
  printf("\nSubtração dos numeros complexos = ");
  compImprimir(sub);
  
  multi = compMultiplicar(n1, n2);
  printf("\nMultiplicação dos numeros complexos = ");
  compImprimir(multi);

  div = compDividir(n1, n2);
  printf("\nDivisão dos numeros complexos = ");
  compImprimir(div);
  
  compLiberar(soma);
  compLiberar(sub);
  compLiberar(multi);
  compLiberar(div);
  compLiberar(n1);
  compLiberar(n2);

  printf("\n\n");
  return 0;
}