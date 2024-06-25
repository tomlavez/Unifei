.data


.text
.globl main
main:
	# Leitura primeiro valor
	li $v0, 5
	syscall
	
	# Valor alocado em a0
	add $a0, $zero, $v0
	
	# Leitura segundo valor
	li $v0, 5
	syscall
	
	# Valor alocado em a1
	add $a1, $zero, $v0
	
	# Chama a função soma
	jal soma
	
	# Aloca o resultado em a0
	la $a0, ($v0)
	li $v0, 1
	syscall
	
	# Finaliza o programa
	li $v0, 10
	syscall
	
.data
.text
soma:
	# aloca os valores em t0 e t1
	move	$t0, $a0	# t0 = A
	move	$t1, $a1	# t1 = B
	li	$t2, 0	#soma
	
	blt	$t1, $t0, troca	# Se B > A, troca
	
loop:	
	add	$t2, $t2, $t0	# soma = soma + A
	addi	$t0, $t0, 1	# A = A + 1
	
	bgt	$t0, $t1, end_loop
	
	j	loop
troca:
	move	$t3, $t0	# temp = A
	move	$t0, $t1	# A = B
	move	$t1, $t3	# B = temp
	
	j loop

end_loop:
	move	$v0, $t2	#v0 = soma
	
	# return
	jr	$ra
	