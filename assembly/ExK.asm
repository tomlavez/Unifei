.data

.text
.globl main
main:
	# Le um valor
	li 	$v0, 5
	syscall
	
	# aloca o valor em a0
	move	$a0, $v0

	# chama a função
	jal	quadrado_perfeito
	
	# aloca o resultado em a0
	move	$a0, $v0

	# imprime o resultado
	li	$v0, 1
	syscall

	# finaliza o programa
	li	$v0, 10
	syscall
	
.data
.text
quadrado_perfeito:
	# aloca o valor em t0
	move	$t0, $a0
	
	li	$t1, 0	# i

loop_quadrado_perfeito:
	move	$t2, $zero	#zerando a variavel
	
	addi	$t1, $t1, 1	# i = i + 1
	mul	$t2, $t1, $t1	# variavel = i * i
	beq	$t2, $t0, sim	# compara variavel com valor buscado
	bgt	$t2, $t0, nao	# verifica se variavel é maior que o valor buscado
	j loop_quadrado_perfeito	# volta pro loop
	
sim:
	li	$v0, 1
	jr	$ra

nao:
	li	$v0, 0
	jr	$ra	
