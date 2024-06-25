.text
.globl main

main:
#Leitura do primeiro número
	li	$v0, 5	#Leitura de inteiros
	syscall
	
	move	$t0, $v0	#Aloca o primeiro valor em t0

#Leitura do segundo numero
	li	$v0, 5	#Leitura de inteiros
	syscall
	
	move	$t1, $v0	#Aloca o Segundo valor em t1

#Leitura do terceiro numero
	li	$v0, 5	#Leitura de inteiros
	syscall
	
	move	$t2, $v0	#Aloca o Terceiro valor em t2
	
#Leitura do quarto numero
	li	$v0, 5	#Leitura de inteiros
	syscall
	
	move	$t3, $v0	#Aloca o Quarto valor em t3

#Localiza o maior

	add	$t4, $t0, $zero	#Define t4 como o maior
	
	#Compara o segundo numero
	slt	$t5, $t4, $t1	#Se o maior for maior, t5 = 0
	beq	$t5, $zero, else1	#Se t5 = 0 pula pro else1	
then1:
	move	$t4, $t1	#Maior vai ser igual o segundo numero
	
else1:
	#Compara o terceiro numero
	slt	$t5, $t4, $t2	#Se o maior for maior, t5 = 0
	beq	$t5, $zero, else2	#Se t5 = 0 pula pro else2
then2:
	move	$t4, $t2	#Maior vai ser igual o terceiro numero
	
else2:
	#Compara o quarto numero
	slt	$t5, $t4, $t3	#Se o maior for maior, t5 = 0
	beq	$t5, $zero, end_if #Se t5 = 0, finaliza os if
then3:
	move	$t4, $t3	#Maior vai ser igual o quarto numero

end_if:
	li	$v0, 1	#Imprime um inteiro
	move	$a0, $t4
	syscall
