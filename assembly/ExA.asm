.data

	maior:	.asciiz "positivo"
	menor:	.asciiz "negativo"

.text
.globl main

main:
	li	$v0, 5	#Leitura de inteiros
	syscall
	
	move $t0, $v0	#Alocando o valor de entrada em v0
	
	li	$v0, 4	#Imprime uma string
	
if1:	slt	$t1, $t0, $zero		#Se o numero for positivo, t1 = 0
	beq 	$t1, $zero, else	#Se t1 for 0, vai pro else
	
then:
	la	$a0, menor
	j end_if
	
else:
	la	$a0, maior
	
end_if:
	syscall
	
#Informa se é positivo ou negativo
