.data


.text
.globl main
main:
	#Lendo um inteiro N
	li $v0, 5
	syscall
	
	move $t0, $v0
	
	#Se for menor ou igual a zero, pula pro fim
	ble $t0, $zero, fim

inicio:
	#Imprime o valor atual
	li $v0, 1
	move $a0, $t0
	syscall
	
	#Encontra o valor anterior
	subi $t0, $t0, 1
	
	#Se o valor anterior for o zero, pula pro fim
	beq $t0, $zero, fim
	
	#Imprime o espaço
	li $v0, 11
	li $a0, 32
	syscall
	
	j inicio
fim: