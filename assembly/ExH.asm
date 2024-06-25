.text
.globl main
main:
	li $v0, 5
	syscall
	
	move $t0, $v0		# move o valor para t0
	
	beq $t0, $zero, caso_zero

	beq $t0, 1, caso_zero

	add $t1, $zero, $t0	# atual
	add $t2, $zero, $t1	# soma = atual
	
for:
	addi $t1, $t1, -1	# atual = atual -1
	beq $t1, 1, fim		# se o prox valor for 1, vai pro fim
	li $t3, 1		# i = 0
	move $t4, $t2
	
for2:
	add $t2, $t2, $t4	# soma = soma + atual
	addi $t3, $t3, 1		# i = i + 1
	beq $t3, $t1, for	# sai do loop se o i == atual
	j for2
	
caso_zero:
	la $t2, 1
	
fim:
	li $v0, 1
	move $a0, $t2
	syscall
	
