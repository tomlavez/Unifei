.text
.globl main
main:
inicio:
	#le um valor inteiro
	li $v0, 5
	syscall
	
	move $t0, $v0
	
	#Se valor for maior que 0, continua
	bgt $t0, $zero, continue
	j inicio
	
continue:
	#Inicializa o contador
	addi $t1, $zero, 1
	#Inicializa a soma
	add $t2, $zero, $t1
	#Se o valor digitado for 1, vai pro fim
	beq $t1, $t0, fim
for:
	#Soma 1 no contador
	addi $t1, $t1, 1
	add $t2, $t2, $t1	#Soma = Soma + contador
	blt $t1, $t0, for
fim:
	#imprime a soma
	li $v0, 1
	move $a0, $t2
	syscall