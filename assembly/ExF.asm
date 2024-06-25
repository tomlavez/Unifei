.text
.globl main
main:
	#Leitura de um inteiro
	li $v0, 5
	syscall
	
	#Aloca o N e t0
	move $t0, $v0
	
	#Inicializa o contador
	li $s0, 0
	
	#Inicializa o primeiro valor
	li $s1, 1
	
	ble $t0, $zero, fim	# Se o valor inserido for menor ou igual a zero, vai pro fim
inicio:

	# Imprime o impar
	li $v0, 1
	move $a0, $s1
	syscall
	
	addi $s0, $s0, 1
	
	#Se o contador foi igual a N
	beq $s0, $t0, fim
	
	#Imprime o espaço
	li $v0, 11
	li $a0, 32
	syscall
	
	# Vai para o próx impar
	addi $s1, $s1, 2
	
	j inicio
fim:
	
	
